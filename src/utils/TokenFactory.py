from datetime import datetime, timedelta

import jwt

from src.entities.User import User
from src.utils.EnvironmentConfig import Config


class JWT:
    blacklisted_tokens = set()

    @staticmethod
    def set_blacklisted_token(token):
        JWT.blacklisted_tokens.add(token)

    @staticmethod
    def generate_admin_token(admin: User):
        return JWT.encode_token(admin.username, Config.ADMIN_SECRET_KEY)

    @staticmethod
    def generate_doctor_token(doctor: User):
        return JWT.encode_token(doctor.username, Config.DOCTOR_SECRET_KEY)

    @staticmethod
    def generate_patient_token(patient: User):
        return JWT.encode_token(patient.username, Config.PATIENT_SECRET_KEY)

    @staticmethod
    def encode_token(username, secret_key):
        return jwt.encode({'username': username, 'exp': datetime.now() + timedelta(hours=1)},
                          secret_key.value, algorithm="HS256")

    @staticmethod
    def decode_token(token, secret_key):
        return jwt.decode(token, secret_key.value, algorithms=["HS256"])

    @staticmethod
    def get_username_from_token(token, secret_key):
        return JWT.decode_token(token, secret_key).get('username')

    @staticmethod
    def is_missing(token):
        return token is None

    @staticmethod
    def is_blacklisted(token):
        return token in JWT.blacklisted_tokens
