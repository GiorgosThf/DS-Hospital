import unittest
from datetime import datetime
from unittest.mock import patch

from src.entities.User import User
from src.services.DoctorService import DoctorService
from src.transfer.accept.ChangeAppointmentCostDto import ChangeAppointmentCostDto
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto
from src.transfer.send.DoctorAppointmentDto import DoctorAppointmentDto
from src.utils.Http import HTTP
from src.utils.ServiceException import ServiceException


class TestDoctorService(unittest.TestCase):

    @patch('src.repositories.DoctorRepository.DoctorRepository.login')
    @patch('src.utils.TokenFactory.JWT.generate_doctor_token')
    def test_login_success(self, MockGenerateToken, MockDoctorLogin):
        # Mock data
        auth_data = User(username='test_doctor', password='test_password')
        MockDoctorLogin.return_value = {'username': 'test_doctor'}

        # Mock JWT token generation
        MockGenerateToken.return_value = 'mock_token'

        # Call method under test
        result = DoctorService.login(auth_data)

        # Assertions
        self.assertEqual(result['username'], 'test_doctor')
        self.assertEqual(result['token'], 'mock_token')

    @patch('src.repositories.DoctorRepository.DoctorRepository.login')
    def test_login_failure(self, MockDoctorLogin):
        # Mock data
        auth_data = User(username='test_doctor', password='wrong_password')
        MockDoctorLogin.return_value = None

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            DoctorService.login(auth_data)

        self.assertEqual(str(context.exception), 'Login failed! User not found!')
        self.assertEqual(context.exception.status_code, HTTP.NOT_FOUND)

    @patch('src.utils.TokenFactory.JWT.is_blacklisted')
    def test_logout_success(self, MockIsBlacklisted):
        # Mock data
        token = 'mock_token'
        MockIsBlacklisted.return_value = True

        # Call method under test
        result = DoctorService.logout(token)

        # Assertions
        self.assertTrue(result)

    @patch('src.utils.TokenFactory.JWT.is_blacklisted')
    def test_logout_failure(self, MockIsBlacklisted):
        # Mock data
        token = 'mock_token'
        MockIsBlacklisted.return_value = False

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            DoctorService.logout(token)

        self.assertEqual(str(context.exception), 'Logout failed')
        self.assertEqual(context.exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    @patch('src.repositories.DoctorRepository.DoctorRepository.update_password')
    def test_update_password_success(self, MockUpdatePassword):
        # Mock data
        current_user = 'test_doctor'
        data = ChangePasswordDto(username=current_user, old_password='old_pass', new_password='new_pass')
        MockUpdatePassword.return_value = True

        # Call method under test
        result = DoctorService.update_password(current_user, data)

        # Assertions
        self.assertTrue(result)

    @patch('src.repositories.DoctorRepository.DoctorRepository.update_password')
    def test_update_password_failure(self, MockUpdatePassword):
        # Mock data
        current_user = 'test_doctor'
        data = ChangePasswordDto(username=current_user, old_password='wrong_pass', new_password='new_pass')
        MockUpdatePassword.return_value = False

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            DoctorService.update_password(current_user, data)

        self.assertEqual(str(context.exception), 'Error updating password')
        self.assertEqual(context.exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    @patch('src.repositories.DoctorRepository.DoctorRepository.update_appointment_cost')
    def test_update_appointment_cost_success(self, MockUpdateAppointmentCost):
        # Mock data
        current_user = 'test_doctor'
        data = ChangeAppointmentCostDto(username=current_user, old_cost=100, new_cost=150)
        MockUpdateAppointmentCost.return_value = True

        # Call method under test
        result = DoctorService.update_appointment_cost(current_user, data)

        # Assertions
        self.assertTrue(result)

    @patch('src.repositories.DoctorRepository.DoctorRepository.update_appointment_cost')
    def test_update_appointment_cost_failure(self, MockUpdateAppointmentCost):
        # Mock data
        current_user = 'test_doctor'
        data = ChangeAppointmentCostDto(username=current_user, old_cost=100, new_cost=150)
        MockUpdateAppointmentCost.return_value = False

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            DoctorService.update_appointment_cost(current_user, data)

        self.assertEqual(str(context.exception), 'Error updating appointment cost')
        self.assertEqual(context.exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    @patch('src.repositories.DoctorRepository.DoctorRepository.fetch_appointments')
    @patch('src.services.DoctorService.DoctorService.get_as_appointments')
    @patch('src.utils.AppointmentScheduler.AppointmentScheduler.is_date_within_rang')
    def test_fetch_appointments(self, MockIsDateWithinRange, MockGetAsAppointments, MockFetchAppointments):
        # Mock data
        current_user = 'test_doctor'
        MockFetchAppointments.return_value = [{'appointment_date': datetime.now()}]
        MockIsDateWithinRange.return_value = True
        MockGetAsAppointments.return_value = [DoctorAppointmentDto(appointment_date=datetime.now())]

        # Call method under test
        result = DoctorService.fetch_appointments(current_user)

        # Assertions
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]['appointment_date'].strftime('%Y-%m-%d'), datetime.now().date().strftime('%Y-%m-%d'))

    def test_get_as_appointments(self):
        # Mock data
        appointments_dto = [{'appointment_date': datetime.now()}]

        # Call method under test
        result = DoctorService.get_as_appointments(appointments_dto)

        # Assertions
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], DoctorAppointmentDto)
        self.assertEqual(result[0].appointment_date, appointments_dto[0]['appointment_date'])


if __name__ == '__main__':
    unittest.main()
