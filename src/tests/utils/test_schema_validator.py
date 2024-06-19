import unittest
from unittest.mock import patch

from src.entities.Specialization import Specialization
from src.utils.SchemaValidator import SchemaValidator
from src.utils.ServiceException import ServiceException


class TestSchemaValidator(unittest.TestCase):

    def setUp(self):
        self.validator = SchemaValidator()

    def test_specialization_validation(self):
        valid_data = {'specialization': Specialization.CARDIOLOGIST.value}
        invalid_data = {'specialization': 'InvalidSpecialization'}

        # Valid specialization
        self.validator.schema = {'specialization': {'type': 'string', 'is_specialization': True}}
        self.assertTrue(self.validator.validate(valid_data))

        # Invalid specialization
        with self.assertRaises(ServiceException):
            self.validator.validate(invalid_data)

    def test_validate_appointment(self):
        valid_appointment = {
            'doctor_username': 'dr_smith',
            'patient_username': 'patient_jane',
            'patient_name': 'Jane',
            'patient_surname': 'Doe',
            'doctor_name': 'John',
            'doctor_surname': 'Smith',
            'appointment_date': '2024-07-01',
            'appointment_time': '10:00',
            'reason': 'Regular checkup',
            'cost': 100.0,
            'specialization': Specialization.CARDIOLOGIST.value
        }

        self.assertTrue(SchemaValidator.validate_appointment(valid_appointment))

    def test_validate_patient_registration(self):
        valid_patient = {
            'username': 'patient_jane',
            'password': 'password123',
            'email': 'jane.doe@example.com',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'amka': '12345678901',
            'date_of_birth': '1990-01-01'
        }

        self.assertTrue(SchemaValidator.validate_patient_registration(valid_patient))

    def test_validate_doctor_registration(self):
        valid_doctor = {
            'username': 'dr_smith',
            'password': 'password123',
            'email': 'dr.smith@example.com',
            'first_name': 'John',
            'last_name': 'Smith',
            'specialization': Specialization.RADIOLOGIST.value,
            'appointment_cost': 100.0
        }

        self.assertTrue(SchemaValidator.validate_doctor_registration(valid_doctor))

    def test_validate_login(self):
        valid_login = {
            'username': 'user1',
            'password': 'password123'
        }

        self.assertTrue(SchemaValidator.validate_login(valid_login))

    def test_validate_password(self):
        valid_password_data = {
            'username': 'user1',
            'old_password': 'oldpassword123',
            'new_password': 'newpassword123'
        }

        self.assertTrue(SchemaValidator.validate_password(valid_password_data))

    def test_validate_appointment_cost(self):
        valid_cost_data = {
            'username': 'user1',
            'old_cost': 100.0,
            'new_cost': 150.0
        }

        self.assertTrue(SchemaValidator.validate_appointment_cost(valid_cost_data))

    def test_validate_appointment_search(self):
        valid_search_data = {
            'appointment_date': '2024-07-01',
            'appointment_time': '10:00',
            'reason': 'Checkup',
            'specialization': Specialization.CARDIOLOGIST.value
        }

        self.assertTrue(SchemaValidator.validate_appointment_search(valid_search_data))

    def test_id_generator(self):
        with patch('random.choices', return_value=['1', '2', '3', '4', '5', '6']):
            result = SchemaValidator.id_generator('PREFIX', 6)
            self.assertEqual(result, 'PREFIX_123456')

    def test_format_validation_errors(self):
        errors = {
            'username': ['required field'],
            'password': ['required field']
        }
        formatted_errors = SchemaValidator.format_validation_errors(errors)
        expected_errors = ['Field: username required field', 'Field: password required field']

        self.assertEqual(formatted_errors, expected_errors)


if __name__ == '__main__':
    unittest.main()
