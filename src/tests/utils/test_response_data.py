import unittest
from datetime import datetime
from unittest.mock import patch

from src.utils.ResponseData import ResponseData


class TestResponseDataBuilder(unittest.TestCase):

    def test_resp_status(self):
        builder = ResponseData.builder()
        builder.resp_status(ResponseData.SUCCESS)
        response = builder.build()

        self.assertEqual(response['status'], ResponseData.SUCCESS)
        self.assertIn('date', response)

    def test_error(self):
        builder = ResponseData.builder()
        error_message = 'An error occurred'
        builder.error(error_message)
        response = builder.build()

        self.assertEqual(response['error'], error_message)
        self.assertIn('date', response)

    def test_resp_data(self):
        builder = ResponseData.builder()
        data = {'key': 'value'}
        builder.resp_data(data)
        response = builder.build()

        self.assertEqual(response['data'], data)
        self.assertIn('date', response)

    def test_combined(self):
        builder = ResponseData.builder()
        status = ResponseData.SUCCESS
        error_message = 'An error occurred'
        data = {'key': 'value'}

        builder.resp_status(status).error(error_message).resp_data(data)
        response = builder.build()

        self.assertEqual(response['status'], status)
        self.assertEqual(response['error'], error_message)
        self.assertEqual(response['data'], data)
        self.assertIn('date', response)

    @patch('src.utils.ResponseData.datetime')
    def test_date_format(self, mock_datetime):
        mock_now = datetime(2024, 6, 19, 12, 0, 0)
        mock_datetime.now.return_value = mock_now

        builder = ResponseData.builder()
        response = builder.build()

        self.assertEqual(response['date'], str(mock_now))


if __name__ == '__main__':
    unittest.main()
