import unittest
from src.transfer.send.DoctorAppointmentDto import DoctorAppointmentDto


class TestDoctorAppointmentDto(unittest.TestCase):

    def test_initialization(self):
        kwargs = {
            'cid': 'doc123',
            'patient_name': 'John',
            'patient_surname': 'Doe',
            'appointment_date': '2024-06-20',
            'appointment_time': '10:00',
            'reason': 'Regular checkup'
        }

        dto = DoctorAppointmentDto(**kwargs)

        # Assertions
        self.assertEqual(dto.cid, 'doc123')
        self.assertEqual(dto.patient_name, 'John')
        self.assertEqual(dto.patient_surname, 'Doe')
        self.assertEqual(dto.appointment_date, '2024-06-20')
        self.assertEqual(dto.appointment_time, '10:00')
        self.assertEqual(dto.reason, 'Regular checkup')

    def test_to_dict(self):
        kwargs = {
            'cid': 'doc123',
            'patient_name': 'John',
            'patient_surname': 'Doe',
            'appointment_date': '2024-06-20',
            'appointment_time': '10:00',
            'reason': 'Regular checkup'
        }
        dto = DoctorAppointmentDto(**kwargs)
        expected_dict = {
            'cid': 'doc123',
            'patient_name': 'John',
            'patient_surname': 'Doe',
            'appointment_time': '10:00',
            'appointment_date': '2024-06-20',
            'reason': 'Regular checkup'
        }
        self.assertEqual(dto.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
