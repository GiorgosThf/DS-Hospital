import unittest
from src.transfer.send.PatientDetailedAppointmentDto import PatientDetailedAppointmentDto


class TestPatientDetailedAppointmentDto(unittest.TestCase):

    def test_initialization(self):
        kwargs = {
            'cid': 'patient123',
            'doctor_name': 'Dr. Smith',
            'doctor_surname': 'Jones',
            'appointment_date': '2024-06-20',
            'appointment_time': '10:00',
            'specialization': 'Cardiology',
            'cost': 100,
            'reason': 'Regular checkup'
        }

        dto = PatientDetailedAppointmentDto(**kwargs)

        # Assertions
        self.assertEqual(dto.cid, 'patient123')
        self.assertEqual(dto.doctor_name, 'Dr. Smith')
        self.assertEqual(dto.doctor_surname, 'Jones')
        self.assertEqual(dto.appointment_date, '2024-06-20')
        self.assertEqual(dto.appointment_time, '10:00')
        self.assertEqual(dto.specialization, 'Cardiology')
        self.assertEqual(dto.cost, 100)
        self.assertEqual(dto.reason, 'Regular checkup')

    def test_to_dict(self):
        kwargs = {
            'cid': 'patient123',
            'doctor_name': 'Dr. Smith',
            'doctor_surname': 'Jones',
            'appointment_date': '2024-06-20',
            'appointment_time': '10:00',
            'specialization': 'Cardiology',
            'cost': 100,
            'reason': 'Regular checkup'
        }
        dto = PatientDetailedAppointmentDto(**kwargs)
        expected_dict = {
            'cid': 'patient123',
            'doctor_name': 'Dr. Smith',
            'doctor_surname': 'Jones',
            'appointment_time': '10:00',
            'appointment_date': '2024-06-20',
            'specialization': 'Cardiology',
            'cost': 100,
            'reason': 'Regular checkup'
        }
        self.assertEqual(dto.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
