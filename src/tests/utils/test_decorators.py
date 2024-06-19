import unittest
from unittest.mock import patch

import jwt
from flask import Flask

from src.entities.ResponseEntity import ResponseEntity
from src.utils.Decorators import token_required, remove_token, handle_exceptions, error_as_response
from src.utils.Http import HTTP
from src.utils.ServiceException import ServiceException, DatabaseException

app = Flask(__name__)


@app.route('/protected')
@token_required(secret_key='test_secret')
def protected_route(current_user):
    return f'Hello, {current_user}!'


class TestDecorators(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    @patch('src.utils.TokenFactory.JWT')
    def test_token_required_valid_token(self, mock_jwt):
        mock_jwt.is_missing.return_value = False
        mock_jwt.is_blacklisted.return_value = False
        mock_jwt.decode_token.return_value = {'username': 'test_user'}

        with app.test_request_context('/protected', headers={'Authorization': 'valid_token'}):
            response = self.client.get('/protected')
            self.assertEqual(200, response.status_code)
            self.assertIn('Hello, test_user!', response.data.decode())

    @patch('src.utils.TokenFactory.JWT')
    def test_token_required_missing_token(self, mock_jwt):
        mock_jwt.is_missing.return_value = True

        with app.test_request_context('/protected'):
            response = self.client.get('/protected')
            self.assertEqual(response.status_code, 403)  # Assuming you return HTTP.FORBIDDEN
            self.assertIn('Token is missing', response.data.decode())

    @patch('src.utils.TokenFactory.JWT')
    def test_token_required_invalid_token(self, mock_jwt):
        mock_jwt.is_missing.return_value = False
        mock_jwt.is_blacklisted.return_value = True

        @token_required('test_secret')
        def test_func(current_user):
            return current_user

        response = test_func()
        self.assertIsInstance(response, ResponseEntity)
        self.assertEqual(response.status, HTTP.UNAUTHORIZED)
        self.assertIn('Token is invalid', response.data.error)

    @patch('src.utils.TokenFactory.JWT')
    def test_token_required_expired_token(self, mock_jwt):
        mock_jwt.is_missing.return_value = False
        mock_jwt.is_blacklisted.return_value = False
        mock_jwt.decode_token.side_effect = jwt.ExpiredSignatureError

        @token_required('test_secret')
        def test_func(current_user):
            return current_user

        response = test_func()
        self.assertIsInstance(response, ResponseEntity)
        self.assertEqual(response.status, HTTP.UNAUTHORIZED)
        self.assertIn('Token is expired', response.data.error)

    @patch('src.utils.TokenFactory.JWT')
    def test_remove_token_valid_token(self, mock_jwt):
        mock_jwt.is_missing.return_value = False
        mock_jwt.decode_token.return_value = {'username': 'test_user'}

        with app.test_request_context('/protected'):

            @remove_token('test_secret')
            def test_func(token):
                return token

            result = test_func('valid_token')

            self.assertEqual(result, 'valid_token')
            mock_jwt.set_blacklisted_token.assert_called_once_with('valid_token')

    @patch('src.utils.TokenFactory.JWT')
    def test_remove_token_missing_token(self, mock_jwt):
        mock_jwt.is_missing.return_value = True

        @remove_token('test_secret')
        def test_func(token):
            return token

        response = test_func(None)
        self.assertIsInstance(response, ResponseEntity)
        self.assertEqual(response.status, HTTP.FORBIDDEN)
        self.assertIn('Token is missing', response.data.error)

    @patch('src.utils.TokenFactory.JWT')
    def test_remove_token_invalid_token(self, mock_jwt):
        mock_jwt.is_missing.return_value = False
        mock_jwt.decode_token.side_effect = jwt.InvalidTokenError

        @remove_token('test_secret')
        def test_func(token):
            return token

        response = test_func('invalid_token')
        self.assertIsInstance(response, ResponseEntity)
        self.assertEqual(response.status, HTTP.UNAUTHORIZED)
        self.assertIn('Token is invalid', response.data.error)

    @patch('src.utils.TokenFactory.JWT')
    def test_remove_token_expired_token(self, mock_jwt):
        mock_jwt.is_missing.return_value = False
        mock_jwt.decode_token.side_effect = jwt.ExpiredSignatureError

        @remove_token('test_secret')
        def test_func(token):
            return token

        response = test_func('expired_token')
        self.assertIsInstance(response, ResponseEntity)
        self.assertEqual(response.status, HTTP.BAD_REQUEST)
        self.assertIn('Token is expired', response.data.error)

    def test_handle_exceptions_service_exception(self):
        exception = ServiceException('Test service exception', status_code=400)

        @handle_exceptions
        def test_func():
            raise exception

        response = test_func()
        self.assertIsInstance(response, ResponseEntity)
        self.assertEqual(response.status, 400)
        self.assertIn('Test service exception', response.data['error'])

    def test_handle_exceptions_generic_exception(self):
        exception = DatabaseException('Test func exception', 200)

        @handle_exceptions
        def test_func():
            raise exception

        response = test_func()
        self.assertIsInstance(response, ResponseEntity)
        self.assertEqual(response.status, 500)
        self.assertIn('Test func exception', response.data['error'])

    def test_error_as_response(self):
        response = error_as_response('Test error message', HTTP.NOT_FOUND)
        self.assertIsInstance(response, ResponseEntity)
        self.assertEqual(response.status, HTTP.NOT_FOUND)
        self.assertIn('Test error message', response.data.error)


if __name__ == '__main__':
    unittest.main()
