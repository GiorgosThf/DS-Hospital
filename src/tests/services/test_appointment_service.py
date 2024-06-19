import unittest
from datetime import datetime
from unittest.mock import patch

from src.services.AppointmentsService import AppointmentService
from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto
from src.transfer.send.DoctorDto import DoctorDto


class TestAppointmentService(unittest.TestCase):

    @patch('src.repositories.DoctorRepository.DoctorRepository.fetch_appointments_by_date')
    @patch('src.utils.AppointmentScheduler.AppointmentScheduler.create_appointment_slots')
    @patch('src.utils.DateUtils.DateTimeUtils')
    def test_check_availability(self, MockDateTimeUtils, MockAppointmentScheduler, MockDoctorRepository):
        # Mock data
        doctor_username = 'test_doctor'
        appointment_date = datetime.now()
        appointments = [
            {'appointment_time': '09:00'},
            {'appointment_time': '10:00'},
            {'appointment_time': '11:00'}
        ]
        available_slots = ['09:00', '10:00', '11:00']

        # Mock DoctorRepository.fetch_appointments_by_date method
        MockDoctorRepository.return_value.fetch_appointments_by_date.return_value = appointments

        # Mock AppointmentScheduler.create_appointment_slots method
        MockAppointmentScheduler.return_value.create_appointment_slots.return_value = available_slots

        # Mock DateTimeUtils methods
        MockDateTimeUtils.date_to_string.return_value = appointment_date.strftime('%Y-%m-%d')
        MockDateTimeUtils.parse_time.side_effect = lambda t, f: datetime.strptime(t, f).time()

        # Call method under test
        result = AppointmentService.check_availability(doctor_username, appointment_date)

        # Assertions
        self.assertEqual(result, [datetime.strptime(slot, '%H:%M').time() for slot in available_slots])

    @patch('src.repositories.DoctorRepository.DoctorRepository.find_by_role')
    @patch('src.services.AppointmentsService.AppointmentService.return_doctors')
    @patch('src.services.AppointmentsService.AppointmentService.check_availability')
    @patch('src.utils.DateUtils.DateTimeUtils')
    def test_find_appointments(self, MockDateTimeUtils, MockCheckAvailability, MockReturnDoctors, MockDoctorRepository):
        # Mock data
        appointment_date = datetime.now().date()
        appointment_time = datetime.now().time()
        search_data = SearchAppointmentDto(appointment_date=appointment_date.strftime('%Y-%m-%d'),
                                           appointment_time=appointment_time.strftime('%H:%M'),
                                           reason="Abdominal Pain", specialization="Hematologist")
        doctors = [{'username': 'test_doctor', 'name': 'Test Doctor'}]
        free_appointments = [appointment_time]

        # Mock DoctorRepository.find_by_role method
        MockDoctorRepository.return_value.find_by_role.return_value = doctors

        # Mock AppointmentService.check_availability method
        MockCheckAvailability.return_value = free_appointments

        # Mock DateTimeUtils methods
        MockDateTimeUtils.parse_time.side_effect = lambda t, f: datetime.strptime(t, f).time()
        MockDateTimeUtils.parse_date.side_effect = lambda d, f: datetime.strptime(d, f).date()

        # Call method under test
        result = AppointmentService.find_appointments(search_data)

        # Assertions
        self.assertIsInstance(result, DoctorDto)
        self.assertEqual(result.username, 'test_doctor')

    def test_return_appointments(self):
        # Mock data
        free_appointments = [datetime.strptime('09:00', '%H:%M').time(),
                             datetime.strptime('10:00', '%H:%M').time(),
                             datetime.strptime('11:00', '%H:%M').time()]

        # Call method under test
        result = AppointmentService.return_appointments(free_appointments)

        # Assertions
        self.assertEqual(result, ['09:00', '10:00', '11:00'])

    def test_return_doctors(self):
        # Mock data
        doctors = [{'username': 'test_doctor', 'first_name': 'Test Doctor'}]

        # Call method under test
        result = AppointmentService.return_doctors(doctors)

        # Assertions
        self.assertIsInstance(result[0], DoctorDto)
        self.assertEqual(result[0].username, 'test_doctor')


if __name__ == '__main__':
    unittest.main()
