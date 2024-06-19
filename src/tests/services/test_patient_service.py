import unittest
from datetime import datetime
from unittest.mock import patch

from src.entities.Patient import Patient
from src.entities.User import User
from src.services.PatientService import PatientService
from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto
from src.transfer.send.DoctorDto import DoctorDto
from src.transfer.send.PatientAppointmentDto import PatientAppointmentDto
from src.utils.Http import HTTP
from src.utils.ServiceException import ServiceException


class TestPatientService(unittest.TestCase):

    @patch('src.repositories.PatientRepository.PatientRepository.exists')
    @patch('src.repositories.PatientRepository.PatientRepository.register')
    @patch('src.utils.TokenFactory.JWT.generate_patient_token')
    def test_register_success(self, MockGenerateToken, MockRegister, MockExists):
        # Mock data
        patient_data = Patient(username='test_patient', password='test_password', email='test@test.com',
                               amka='test', date_of_birth='test_date_of_birth', first_name='test_first_name',
                               last_name='test_last_name')
        MockExists.return_value = False
        MockRegister.return_value = patient_data.to_db()
        MockGenerateToken.return_value = 'mock_token'

        # Call method under test
        result = PatientService.register(patient_data)

        # Assertions
        self.assertEqual(result['username'], 'test_patient')
        self.assertEqual(result['token'], 'mock_token')

    @patch('src.repositories.PatientRepository.PatientRepository.exists')
    def test_register_failure(self, MockExists):
        # Mock data
        patient_data = Patient(username='test_patient', password='test_password', email='test@test.com',
                               amka='test', date_of_birth='test_date_of_birth', first_name='test_first_name',
                               last_name='test_last_name')
        MockExists.return_value = True

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            PatientService.register(patient_data)

        self.assertEqual(str(context.exception),
                         'Error during registration, Patient with username test_patient and email test@test.com already exists')
        self.assertEqual(context.exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    @patch('src.repositories.PatientRepository.PatientRepository.login')
    @patch('src.utils.TokenFactory.JWT.generate_patient_token')
    def test_login_success(self, MockGenerateToken, MockLogin):
        # Mock data
        auth_data = User(username='test_patient', password='test_password')
        MockLogin.return_value = {'username': 'test_patient'}
        MockGenerateToken.return_value = 'mock_token'

        # Call method under test
        result = PatientService.login(auth_data)

        # Assertions
        self.assertEqual(result['username'], 'test_patient')
        self.assertEqual(result['token'], 'mock_token')

    @patch('src.repositories.PatientRepository.PatientRepository.login')
    def test_login_failure(self, MockLogin):
        # Mock data
        auth_data = User(username='test_patient', password='wrong_password')
        MockLogin.return_value = None

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            PatientService.login(auth_data)

        self.assertEqual(str(context.exception), 'Login failed! User not found!')
        self.assertEqual(context.exception.status_code, HTTP.NOT_FOUND)

    @patch('src.utils.TokenFactory.JWT.is_blacklisted')
    def test_logout_success(self, MockIsBlacklisted):
        # Mock data
        token = 'mock_token'
        MockIsBlacklisted.return_value = True

        # Call method under test
        result = PatientService.logout(token)

        # Assertions
        self.assertTrue(result)

    @patch('src.utils.TokenFactory.JWT.is_blacklisted')
    def test_logout_failure(self, MockIsBlacklisted):
        # Mock data
        token = 'mock_token'
        MockIsBlacklisted.return_value = False

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            PatientService.logout(token)

        self.assertEqual(str(context.exception), 'Logout failed')
        self.assertEqual(context.exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    @patch('src.services.AppointmentsService.AppointmentService.check_time')
    @patch('src.services.AppointmentsService.AppointmentService.check_date')
    @patch('src.services.AppointmentsService.AppointmentService.find_appointments')
    @patch('src.repositories.PatientRepository.PatientRepository.find_by_username')
    @patch('src.repositories.PatientRepository.PatientRepository.book_appointment')
    @patch('src.services.AppointmentsService.AppointmentService.check_availability')
    def test_book_appointment_success(self, MockCheckAvailability, MockBookAppointment, MockFindByUsername,
                                      MockFindAppointments, MockCheckDate, MockCheckTime):
        # Mock data
        current_user = 'test_patient'
        appointment_data = SearchAppointmentDto(appointment_time='10:00', appointment_date='2024-07-01',
                                                specialization='Cardiologist', reason='test_patient')
        doctor_dto = DoctorDto(username='test_doctor', specialization='Cardiologist')
        MockCheckTime.return_value = True
        MockCheckDate.return_value = True
        MockFindAppointments.return_value = doctor_dto
        MockCheckAvailability.return_value = [(10, 0)]

        # Call method under test
        result = PatientService.book_appointment(current_user, appointment_data)

        # Assertions
        self.assertIn('cid', result)
        self.assertEqual(result['patient_username'], 'test_patient')
        self.assertEqual(result['doctor_username'], 'test_doctor')
        self.assertEqual(result['appointment_time'], '10:00')
        self.assertEqual(result['appointment_date'], '2024-07-01')

    @patch('src.services.AppointmentsService.AppointmentService.check_time')
    def test_book_appointment_time_outside_working_hours(self, MockCheckTime):
        # Mock data
        current_user = 'test_patient'
        appointment_data = SearchAppointmentDto(appointment_time='07:00', appointment_date='2024-07-01',
                                                specialization='Cardiologist', reason='None')
        MockCheckTime.return_value = False

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            PatientService.book_appointment(current_user, appointment_data)

        self.assertEqual(str(context.exception), 'Appointment time is outside working hours')
        self.assertEqual(context.exception.status_code, HTTP.BAD_REQUEST)

    @patch('src.services.AppointmentsService.AppointmentService.check_time')
    @patch('src.services.AppointmentsService.AppointmentService.check_date')
    @patch('src.services.AppointmentsService.AppointmentService.find_appointments')
    @patch('src.services.AppointmentsService.AppointmentService.check_availability')
    def test_book_appointment_no_available_doctors(self, MockCheckAvailability, MockFindAppointments,
                                                   MockCheckDate, MockCheckTime):
        # Mock data
        current_user = 'test_patient'
        appointment_data = SearchAppointmentDto(appointment_time='10:00', appointment_date='2024-07-01',
                                                reason='test_patient', specialization='Cardiologist')
        MockCheckTime.return_value = True
        MockCheckDate.return_value = True
        MockFindAppointments.return_value = None

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            PatientService.book_appointment(current_user, appointment_data)

        self.assertEqual(str(context.exception), 'Not any available appointments found')
        self.assertEqual(context.exception.status_code, HTTP.BAD_REQUEST)

    @patch('src.services.AppointmentsService.AppointmentService.check_time')
    @patch('src.services.AppointmentsService.AppointmentService.check_date')
    @patch('src.services.AppointmentsService.AppointmentService.find_appointments')
    @patch('src.services.AppointmentsService.AppointmentService.check_availability')
    def test_book_appointment_time_not_available(self, MockCheckAvailability, MockFindAppointments,
                                                 MockCheckDate, MockCheckTime):
        # Mock data
        current_user = 'test_patient'
        appointment_data = SearchAppointmentDto(appointment_time='10:00', appointment_date='2024-07-01',
                                                reason='test_patient', specialization='Cardiologist')
        doctor_dto = DoctorDto(username='test_doctor')
        MockCheckTime.return_value = True
        MockCheckDate.return_value = True
        MockFindAppointments.return_value = doctor_dto
        MockCheckAvailability.return_value = []

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            PatientService.book_appointment(current_user, appointment_data)

        self.assertEqual(str(context.exception),
                         'Appointment time is not available for selected date other free slots are available')
        self.assertEqual(context.exception.status_code, HTTP.BAD_REQUEST)

    @patch('src.repositories.PatientRepository.PatientRepository.fetch_appointments')
    @patch('src.services.PatientService.PatientService.get_as_appointments')
    @patch('src.services.AppointmentsService.AppointmentService.check_availability')
    def test_fetch_appointments(self, MockIsDateWithinRange, MockGetAsAppointments, MockFetchAppointments):
        # Mock data
        current_user = 'test_patient'
        MockFetchAppointments.return_value = [{'appointment_date': '2024-09-12'}]
        MockIsDateWithinRange.return_value = True
        MockGetAsAppointments.return_value = [PatientAppointmentDto(appointment_date='2024-09-12')]

        # Call method under test
        result = PatientService.fetch_appointments(current_user)

        # Assertions
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]['appointment_date'], '2024-09-12')

    @patch('src.repositories.PatientRepository.PatientRepository.fetch_appointment_details')
    def test_fetch_appointment_details_success(self, MockFetchAppointmentDetails):
        # Mock data
        current_user = 'test_patient'
        appointment_id = 123
        MockFetchAppointmentDetails.return_value = {'cid': appointment_id}

        # Call method under test
        result = PatientService.fetch_appointment_details(current_user, appointment_id)

        # Assertions
        self.assertEqual(result['cid'], 123)

    @patch('src.repositories.PatientRepository.PatientRepository.fetch_appointment_details')
    def test_fetch_appointment_details_failure(self, MockFetchAppointmentDetails):
        # Mock data
        current_user = 'test_patient'
        appointment_id = 123
        MockFetchAppointmentDetails.return_value = None

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            PatientService.fetch_appointment_details(current_user, appointment_id)

        self.assertEqual(str(context.exception), 'Error fetching patient appointment')
        self.assertEqual(context.exception.status_code, HTTP.NOT_FOUND)

    @patch('src.repositories.PatientRepository.PatientRepository.cancel_appointment')
    def test_cancel_appointment_success(self, MockCancelAppointment):
        # Mock data
        current_user = 'test_patient'
        appointment_id = 123
        MockCancelAppointment.return_value = True

        # Call method under test
        result = PatientService.cancel_appointment(current_user, appointment_id)

        # Assertions
        self.assertTrue(result)

    @patch('src.repositories.PatientRepository.PatientRepository.cancel_appointment')
    def test_cancel_appointment_failure(self, MockCancelAppointment):
        # Mock data
        current_user = 'test_patient'
        appointment_id = 123
        MockCancelAppointment.return_value = False

        # Call method under test and assert ServiceException
        with self.assertRaises(ServiceException) as context:
            PatientService.cancel_appointment(current_user, appointment_id)

        self.assertEqual(str(context.exception), 'Error deleting patient')
        self.assertEqual(context.exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    def test_get_as_appointments(self):
        # Mock data
        appointments_dto = [{'appointment_date': datetime.now()}]

        # Call method under test
        result = PatientService.get_as_appointments(appointments_dto)

        # Assertions
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], PatientAppointmentDto)
        self.assertEqual(result[0].appointment_date, appointments_dto[0]['appointment_date'])


if __name__ == '__main__':
    unittest.main()
