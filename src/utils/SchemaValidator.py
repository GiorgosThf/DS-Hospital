import random
import string

from cerberus import Validator

from src.entities.Specialization import Specialization
from src.utils.ServiceException import ServiceException


class SchemaValidator(Validator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema_registry.add('is_specialization', {'type': 'boolean'})

    def _validate_is_specialization(self, is_specialization, field, value):
        """{'type': 'boolean'}"""
        if is_specialization and not any(value == item.value for item in Specialization):
            self._error(field, f"{value} is not a valid specialization")

    def validate(self, data):
        is_valid = super().validate(data)

        if is_valid:
            return is_valid

        raise ServiceException(super().errors, 500)

    @staticmethod
    def format_validation_errors(errors):
        formatted_errors = []
        for field, messages in errors.items():
            for message in messages:
                formatted_errors.append(f"Field: {field} {message}")
        return formatted_errors


    @staticmethod
    def validate_appointment(data):
        schema = {
            '_id': {'type': 'string', 'required': False},
            'doctor_username': {'type': 'string', 'required': True},
            'patient_username': {'type': 'string', 'required': True},
            'patient_name': {'type': 'string', 'required': True},
            'patient_surname': {'type': 'string', 'required': True},
            'doctor_name': {'type': 'string', 'required': True},
            'doctor_surname': {'type': 'string', 'required': True},
            'appointment_date': {'type': 'string', 'required': True},
            'appointment_time': {'type': 'string', 'required': True},
            'reason': {'type': 'string', 'required': True},
            'cost': {'type': 'float', 'required': True},
            "specialization": {'type': 'string', 'required': True, 'is_specialization': True},
        }
        return SchemaValidator(schema).validate(data)

    @staticmethod
    def validate_patient_registration(data):
        schema = {
            'username': {'type': 'string', 'required': True},
            'password': {'type': 'string', 'required': True},
            'email': {'type': 'string', 'required': True, 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
            'first_name': {'type': 'string', 'required': True},
            'last_name': {'type': 'string', 'required': True},
            'amka': {'type': 'string', 'required': True},
            'date_of_birth': {'type': 'string', 'required': True}
        }
        return SchemaValidator(schema).validate(data)

    @staticmethod
    def validate_doctor_registration(data):
        schema = {
            'username': {'type': 'string', 'required': True},
            'password': {'type': 'string', 'required': True},
            'email': {'type': 'string', 'required': True, 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
            'first_name': {'type': 'string', 'required': True},
            'last_name': {'type': 'string', 'required': True},
            'specialization': {'type': 'string',
                               'required': True,
                               'is_specialization': True
                               },
            'appointment_cost': {'type': 'float', 'required': True}
        }
        return SchemaValidator(schema).validate(data)

    @staticmethod
    def validate_login(data):
        print(data)
        schema = {
            'username': {'type': 'string', 'required': True},
            'password': {'type': 'string', 'required': True},
        }
        return SchemaValidator(schema).validate(data)

    @staticmethod
    def validate_password(data):
        schema = {
            'username': {'type': 'string', 'required': True},
            'old_password': {'type': 'string', 'required': True},
            'new_password': {'type': 'string', 'required': True},
        }

        return SchemaValidator(schema).validate(data)

    @staticmethod
    def validate_appointment_cost(data):
        schema = {
            'username': {'type': 'string', 'required': True},
            'old_cost': {'type': 'float', 'required': True},
            'new_cost': {'type': 'float', 'required': True},
        }
        return SchemaValidator(schema).validate(data)

    @staticmethod
    def validate_appointment_search(json):
        schema = {
            'appointment_date': {'type': 'string', 'required': True},
            'appointment_time': {'type': 'string', 'required': True},
            'reason': {'type': 'string', 'required': True},
            'specialization': {'type': 'string', 'required': True, 'is_specialization': True},
        }
        return SchemaValidator(schema).validate(json)

    @staticmethod
    def id_generator(prefix, length: int):
        random_number = ''.join(random.choices(string.digits, k=length))
        return f"{prefix}_{random_number}"


class DataValidation:
    def __init__(self, is_valid, errors=None):
        self.is_valid = is_valid
        self.errors = errors
