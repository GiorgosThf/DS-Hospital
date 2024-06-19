import unittest
from unittest.mock import patch

from bson import ObjectId

from src.entities.Doctor import Doctor
from src.entities.User import User
from src.repositories.AdminRepository import AdminRepository
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto


class TestAdminRepository(unittest.TestCase):

    @patch('src.repositories.AdminRepository.ADMIN_COLLECTION')
    def test_login_success(self, mock_admin_collection):
        mock_admin = {'username': 'admin', 'password': 'password123'}
        mock_admin_collection.find_one.return_value = mock_admin

        auth_data = User(username='admin', password='password123')
        result = AdminRepository.login(auth_data)

        self.assertIsNotNone(result)
        self.assertEqual(result['username'], 'admin')

    @patch('src.repositories.AdminRepository.ADMIN_COLLECTION')
    def test_login_failure(self, mock_admin_collection):
        mock_admin_collection.find_one.return_value = None

        auth_data = User(username='admin', password='password123')
        result = AdminRepository.login(auth_data)

        self.assertIsNone(result)

    @patch('src.repositories.AdminRepository.DOCTOR_COLLECTION')
    def test_create_doctor_success(self, mock_doctor_collection):
        doctor_data = {'username': 'doctor', 'email': 'doctor@example.com'}
        mock_doctor_collection.insert_one.return_value.inserted_id = ObjectId()
        mock_doctor_collection.find_one.return_value = doctor_data

        result = AdminRepository.create_doctor(doctor_data)

        self.assertIsNotNone(result)
        self.assertEqual(result['username'], 'doctor')

    @patch('src.repositories.AdminRepository.DOCTOR_COLLECTION')
    def test_create_doctor_failure(self, mock_doctor_collection):
        doctor_data = {'username': 'doctor', 'email': 'doctor@example.com'}
        mock_doctor_collection.insert_one.return_value.inserted_id = None

        result = AdminRepository.create_doctor(doctor_data)

        self.assertIsNone(result)

    @patch('src.repositories.AdminRepository.DOCTOR_COLLECTION')
    def test_delete_doctor_success(self, mock_doctor_collection):
        mock_doctor_collection.delete_one.return_value.deleted_count = 1

        result = AdminRepository.delete_doctor('doctor')

        self.assertTrue(result)

    @patch('src.repositories.AdminRepository.DOCTOR_COLLECTION')
    def test_delete_doctor_failure(self, mock_doctor_collection):
        mock_doctor_collection.delete_one.return_value.deleted_count = 0

        result = AdminRepository.delete_doctor('doctor')

        self.assertFalse(result)

    @patch('src.repositories.AdminRepository.DOCTOR_COLLECTION')
    def test_update_doctor_password_success(self, mock_doctor_collection):
        mock_doctor = {'username': 'doctor', 'password': 'old_password'}
        mock_doctor_collection.find_one.return_value = mock_doctor
        mock_doctor_collection.update_one.return_value.modified_count = 1

        data = ChangePasswordDto(username='doctor', old_password='old_password', new_password='new_password')
        result = AdminRepository.update_doctor_password(data)

        self.assertTrue(result)

    @patch('src.repositories.AdminRepository.DOCTOR_COLLECTION')
    def test_update_doctor_password_failure(self, mock_doctor_collection):
        mock_doctor_collection.find_one.return_value = None

        data = ChangePasswordDto(username='doctor', old_password='old_password', new_password='new_password')
        result = AdminRepository.update_doctor_password(data)

        self.assertFalse(result)

    @patch('src.repositories.AdminRepository.PATIENT_COLLECTION')
    def test_delete_patient_success(self, mock_patient_collection):
        mock_patient_collection.delete_one.return_value.deleted_count = 1

        result = AdminRepository.delete_patient('patient')

        self.assertTrue(result)

    @patch('src.repositories.AdminRepository.PATIENT_COLLECTION')
    def test_delete_patient_failure(self, mock_patient_collection):
        mock_patient_collection.delete_one.return_value.deleted_count = 0

        result = AdminRepository.delete_patient('patient')

        self.assertFalse(result)

    @patch('src.repositories.AdminRepository.DOCTOR_COLLECTION')
    def test_doctor_exists(self, mock_doctor_collection):
        doctor_data = Doctor(username='doctor', password="root",  email='doctor@example.com',
                             first_name="Smith", last_name="Doe", specialization="Cardiologist", appointment_cost=200)
        mock_doctor_collection.find_one.return_value = doctor_data

        result = AdminRepository.doctor_exists(doctor_data)

        self.assertTrue(result)

    @patch('src.repositories.AdminRepository.DOCTOR_COLLECTION')
    def test_doctor_not_exists(self, mock_doctor_collection):
        doctor_data = Doctor(username='doctor', password="root",  email='doctor@example.com',
                             first_name="Smith", last_name="Doe", specialization="Cardiologist", appointment_cost=200)
        mock_doctor_collection.find_one.return_value = None

        result = AdminRepository.doctor_exists(doctor_data)

        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
