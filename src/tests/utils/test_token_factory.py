import unittest
from datetime import datetime, timedelta

import jwt

from src.entities.User import User
from src.utils.EnvironmentConfig import Config
from src.utils.TokenFactory import JWT


class TestJWT(unittest.TestCase):

    def test_generate_admin_token(self):
        admin = User(username='admin_user', password='password')
        token = JWT.generate_admin_token(admin)

        decoded = jwt.decode(token, 'admin_secret_key', algorithms=["HS256"])
        self.assertEqual(decoded['username'], 'admin_user')

    def test_generate_doctor_token(self):
        doctor = User(username='doctor_user', password='password')
        token = JWT.generate_doctor_token(doctor)

        decoded = jwt.decode(token, 'doctor_secret_key', algorithms=["HS256"])
        self.assertEqual(decoded['username'], 'doctor_user')

    def test_generate_patient_token(self):
        patient = User(username='patient_user', password='password')
        token = JWT.generate_patient_token(patient)

        decoded = jwt.decode(token, 'patient_secret_key', algorithms=["HS256"])
        self.assertEqual(decoded['username'], 'patient_user')

    def test_encode_token(self):
        token = JWT.encode_token('test_user', Config.ADMIN_SECRET_KEY)

        decoded = jwt.decode(token, 'admin_secret_key', algorithms=["HS256"])
        self.assertEqual(decoded['username'], 'test_user')
        self.assertIn('exp', decoded)

    def test_decode_token(self):
        token = jwt.encode({'username': 'test_user', 'exp': datetime.now() + timedelta(hours=1)}, 'admin_secret_key',
                           algorithm="HS256")
        decoded = JWT.decode_token(token, Config.ADMIN_SECRET_KEY)

        self.assertEqual(decoded['username'], 'test_user')

    def test_get_username_from_token(self):
        token = jwt.encode({'username': 'test_user', 'exp': datetime.now() + timedelta(hours=1)}, 'admin_secret_key',
                           algorithm="HS256")
        username = JWT.get_username_from_token(token, Config.ADMIN_SECRET_KEY)

        self.assertEqual(username, 'test_user')

    def test_is_missing(self):
        self.assertTrue(JWT.is_missing(None))
        self.assertFalse(JWT.is_missing('token'))

    def test_is_blacklisted(self):
        token = 'blacklisted_token'
        JWT.set_blacklisted_token(token)

        self.assertTrue(JWT.is_blacklisted(token))
        self.assertFalse(JWT.is_blacklisted('another_token'))


if __name__ == '__main__':
    unittest.main()
