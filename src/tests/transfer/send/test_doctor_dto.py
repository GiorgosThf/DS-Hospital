import unittest
from src.transfer.send.DoctorDto import DoctorDto


class TestDoctorDto(unittest.TestCase):

    def test_initialization(self):
        kwargs = {
            '_id': '123',
            'username': 'doctor_user',
            'password': 'doctor_pass',
            'email': 'doctor@example.com',
            'first_name': 'Doctor',
            'last_name': 'User',
            'specialization': 'Cardiology',
            'appointment_cost': 100,
            'cid': 'doc123'
        }

        dto = DoctorDto(**kwargs)

        # Assertions
        self.assertEqual(dto._id, '123')
        self.assertEqual(dto.username, 'doctor_user')
        self.assertEqual(dto.password, 'doctor_pass')
        self.assertEqual(dto.email, 'doctor@example.com')
        self.assertEqual(dto.first_name, 'Doctor')
        self.assertEqual(dto.last_name, 'User')
        self.assertEqual(dto.specialization, 'Cardiology')
        self.assertEqual(dto.appointment_cost, 100)
        self.assertEqual(dto.cid, 'doc123')

    def test_to_dict(self):
        kwargs = {
            '_id': '123',
            'username': 'doctor_user',
            'password': 'doctor_pass',
            'email': 'doctor@example.com',
            'first_name': 'Doctor',
            'last_name': 'User',
            'specialization': 'Cardiology',
            'appointment_cost': 100,
            'cid': 'doc123'
        }
        dto = DoctorDto(**kwargs)
        expected_dict = {
            'cid': 'doc123',
            'username': 'doctor_user',
            'email': 'doctor@example.com',
            'first_name': 'Doctor',
            'last_name': 'User',
            'specialization': 'Cardiology',
            'appointment_cost': 100
        }
        self.assertEqual(dto.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
