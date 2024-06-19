import unittest
from unittest.mock import patch

from src.entities.User import User
from src.repositories.DoctorRepository import DoctorRepository
from src.transfer.accept.ChangeAppointmentCostDto import ChangeAppointmentCostDto
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto
from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto


class TestDoctorRepository(unittest.TestCase):

    @patch('src.repositories.DoctorRepository.DOCTOR_COLLECTION')
    def test_login_success(self, mock_doctor_collection):
        mock_doctor = {'username': 'doctor', 'password': 'password123'}
        mock_doctor_collection.find_one.return_value = mock_doctor

        auth_data = User(username='doctor', password='password123')
        result = DoctorRepository.login(auth_data)

        self.assertIsNotNone(result)
        self.assertEqual(result['username'], 'doctor')

    @patch('src.repositories.DoctorRepository.DOCTOR_COLLECTION')
    def test_login_failure(self, mock_doctor_collection):
        mock_doctor_collection.find_one.return_value = None

        auth_data = User(username='doctor', password='password123')
        result = DoctorRepository.login(auth_data)

        self.assertIsNone(result)

    @patch('src.repositories.DoctorRepository.DOCTOR_COLLECTION')
    def test_update_password_success(self, mock_doctor_collection):
        mock_doctor = {'username': 'doctor', 'password': 'old_password'}
        mock_doctor_collection.find_one.return_value = mock_doctor
        mock_doctor_collection.update_one.return_value.modified_count = 1

        data = ChangePasswordDto(username='doctor', old_password='old_password', new_password='new_password')
        result = DoctorRepository.update_password('doctor', data)

        self.assertTrue(result)

    @patch('src.repositories.DoctorRepository.DOCTOR_COLLECTION')
    def test_update_password_failure(self, mock_doctor_collection):
        mock_doctor_collection.find_one.return_value = None

        data = ChangePasswordDto(username='doctor', old_password='old_password', new_password='new_password')
        result = DoctorRepository.update_password('doctor', data)

        self.assertFalse(result)

    @patch('src.repositories.DoctorRepository.DOCTOR_COLLECTION')
    def test_update_appointment_cost_success(self, mock_doctor_collection):
        mock_doctor = {'username': 'doctor', 'appointment_cost': 100}
        mock_doctor_collection.find_one.return_value = mock_doctor
        mock_doctor_collection.update_one.return_value.modified_count = 1

        data = ChangeAppointmentCostDto(username='doctor', old_cost=100, new_cost=150)
        result = DoctorRepository.update_appointment_cost('doctor', data)

        self.assertTrue(result)

    @patch('src.repositories.DoctorRepository.DOCTOR_COLLECTION')
    def test_update_appointment_cost_failure(self, mock_doctor_collection):
        mock_doctor_collection.find_one.return_value = None

        data = ChangeAppointmentCostDto(username='doctor', old_cost=100, new_cost=150)
        result = DoctorRepository.update_appointment_cost('doctor', data)

        self.assertFalse(result)

    @patch('src.repositories.DoctorRepository.APPOINTMENT_COLLECTION')
    def test_fetch_appointments(self, mock_appointment_collection):
        mock_appointments = [{'doctor_username': 'doctor', 'appointment_date': '2023-06-18'}]
        mock_appointment_collection.find.return_value = mock_appointments

        result = DoctorRepository.fetch_appointments('doctor')

        self.assertEqual(result, mock_appointments)

    @patch('src.repositories.DoctorRepository.APPOINTMENT_COLLECTION')
    def test_fetch_appointments_by_date(self, mock_appointment_collection):
        mock_appointments = [{'doctor_username': 'doctor', 'appointment_date': '2023-06-18'}]
        mock_appointment_collection.find.return_value = mock_appointments

        result = DoctorRepository.fetch_appointments_by_date('doctor', '2023-06-18')

        self.assertEqual(result, mock_appointments)

    @patch('src.repositories.DoctorRepository.DOCTOR_COLLECTION')
    def test_find_by_role(self, mock_doctor_collection):
        mock_doctors = [{'username': 'doctor', 'specialization': 'cardiology'}]
        mock_doctor_collection.find.return_value = mock_doctors

        data = SearchAppointmentDto(appointment_date="2024-08-20", appointment_time="09:00",
                                    specialization='Cardiologist', reason="General Checkup")
        result = DoctorRepository.find_by_role(data)

        self.assertEqual(result, mock_doctors)


if __name__ == '__main__':
    unittest.main()
