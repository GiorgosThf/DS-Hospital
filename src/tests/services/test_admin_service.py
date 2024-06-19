import unittest
from unittest.mock import patch

from src.entities.Doctor import Doctor
from src.entities.User import User
from src.services.AdminService import AdminService
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto
from src.utils.Http import HTTP
from src.utils.ServiceException import ServiceException


class TestAdminService(unittest.TestCase):

    @patch('src.services.AdminService.AdminRepository')
    @patch('src.utils.TokenFactory.JWT')
    def test_login_success(self, MockJWT, MockAdminRepository):
        # Mocking AdminRepository login method
        MockAdminRepository.login.return_value = True

        # Mocking JWT generate_admin_token method
        MockJWT.generate_admin_token.return_value = 'mock_token'

        auth_data = User(username='admin', password='adminpass')
        result = AdminService.login(auth_data)

        # Assertions
        self.assertTrue(result)
        self.assertEqual(result['username'], 'admin')
        self.assertEqual(result['token'], 'mock_token')

    @patch('src.services.AdminService.AdminRepository')
    @patch('src.utils.TokenFactory.JWT')
    def test_login_failure(self, MockJWT, MockAdminRepository):
        # Mocking AdminRepository login method
        MockAdminRepository.login.return_value = False

        auth_data = User(username='nonexistent', password='invalidpass')

        with self.assertRaises(ServiceException) as cm:
            AdminService.login(auth_data)

        self.assertEqual(str(cm.exception), 'Login failed! User not found!')
        self.assertEqual(cm.exception.status_code, HTTP.NOT_FOUND)

    @patch('src.utils.TokenFactory.JWT')
    def test_logout(self, MockJWT):
        # Mocking JWT is_blacklisted method
        MockJWT.is_blacklisted.return_value = True

        token = 'mock_token'
        result = AdminService.logout(token)

        # Assertions
        self.assertTrue(result)

    @patch('src.services.AdminService.AdminRepository')
    def test_delete_doctor_success(self, MockAdminRepository):
        # Mocking AdminRepository delete_doctor method
        MockAdminRepository.delete_doctor.return_value = True

        username = 'doctor1'
        result = AdminService.delete_doctor(username)

        # Assertions
        self.assertTrue(result)

    @patch('src.services.AdminService.AdminRepository')
    def test_delete_doctor_failure(self, MockAdminRepository):
        # Mocking AdminRepository delete_doctor method
        MockAdminRepository.delete_doctor.return_value = False

        username = 'nonexistent_doctor'

        with self.assertRaises(ServiceException) as cm:
            AdminService.delete_doctor(username)

        self.assertEqual(str(cm.exception), 'Error deleting doctor')
        self.assertEqual(cm.exception.status_code, HTTP.NOT_FOUND)

    @patch('src.services.AdminService.AdminRepository')
    def test_update_doctor_password_success(self, MockAdminRepository):
        # Mocking AdminRepository update_doctor_password method
        MockAdminRepository.update_doctor_password.return_value = True

        change_password_data = ChangePasswordDto(username='doctor1', old_password='oldpass', new_password='newpass')
        result = AdminService.update_doctor_password(change_password_data)

        # Assertions
        self.assertTrue(result)

    @patch('src.services.AdminService.AdminRepository')
    def test_update_doctor_password_failure(self, MockAdminRepository):
        # Mocking AdminRepository update_doctor_password method
        MockAdminRepository.update_doctor_password.return_value = False

        change_password_data = ChangePasswordDto(username='nonexistent_doctor', old_password='oldpass', new_password='newpass')

        with self.assertRaises(ServiceException) as cm:
            AdminService.update_doctor_password(change_password_data)

        self.assertEqual(str(cm.exception), 'Error updating doctor password')
        self.assertEqual(cm.exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    @patch('src.services.AdminService.AdminRepository')
    def test_create_doctor_success(self, MockAdminRepository):
        # Mocking AdminRepository doctor_exists and create_doctor methods
        MockAdminRepository.doctor_exists.return_value = False
        MockAdminRepository.create_doctor.return_value = {'username': 'doctor', 'email': 'doctor@example.com'}

        doctor_data = Doctor(username='doctor', password="root",  email='doctor@example.com',
                             first_name="Smith", last_name="Doe", specialization="Cardiologist", appointment_cost=200)
        result = AdminService.create_doctor(doctor_data)

        # Assertions
        self.assertEqual(result['username'], 'doctor')
        self.assertEqual(result['email'], 'doctor@example.com')

    @patch('src.services.AdminService.AdminRepository')
    def test_create_doctor_failure(self, MockAdminRepository):
        # Mocking AdminRepository doctor_exists method
        MockAdminRepository.doctor_exists.return_value = True

        doctor_data = Doctor(username='doctor', password="root",  email='doctor@example.com',
                             first_name="Smith", last_name="Doe", specialization="Cardiologist", appointment_cost=200)

        with self.assertRaises(ServiceException) as cm:
            AdminService.create_doctor(doctor_data)

        expected_message = ("Error creating doctor, Doctor with username doctor "
                            "and email doctor@example.com already exists")
        self.assertEqual(str(cm.exception), expected_message)
        self.assertEqual(cm.exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    @patch('src.services.AdminService.AdminRepository')
    def test_delete_patient_success(self, MockAdminRepository):
        # Mocking AdminRepository delete_patient method
        MockAdminRepository.delete_patient.return_value = True

        username = 'patient1'
        result = AdminService.delete_patient(username)

        # Assertions
        self.assertTrue(result)

    @patch('src.services.AdminService.AdminRepository')
    def test_delete_patient_failure(self, MockAdminRepository):
        # Mocking AdminRepository delete_patient method
        MockAdminRepository.delete_patient.return_value = False

        username = 'nonexistent_patient'

        with self.assertRaises(ServiceException) as cm:
            AdminService.delete_patient(username)

        self.assertEqual(str(cm.exception), 'Error deleting patient')
        self.assertEqual(cm.exception.status_code, HTTP.INTERNAL_SERVER_ERROR)


if __name__ == '__main__':
    unittest.main()

