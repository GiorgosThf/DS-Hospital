import unittest
from src.transfer.send.PatientDto import PatientDto


class TestPatientDto(unittest.TestCase):

    def test_initialization(self):
        kwargs = {
            '_id': '456',
            'username': 'patient_user',
            'password': 'patient_pass',
            'email': 'patient@example.com',
            'first_name': 'Patient',
            'last_name': 'User',
            'amka': '1234567890',
            'date_of_birth': '2000-01-01',
            'cid': 'pat456'
        }

        dto = PatientDto(**kwargs)

        # Assertions
        self.assertEqual(dto._id, '456')
        self.assertEqual(dto.username, 'patient_user')
        self.assertEqual(dto.password, 'patient_pass')
        self.assertEqual(dto.email, 'patient@example.com')
        self.assertEqual(dto.first_name, 'Patient')
        self.assertEqual(dto.last_name, 'User')
        self.assertEqual(dto.amka, '1234567890')
        self.assertEqual(dto.date_of_birth, '2000-01-01')
        self.assertEqual(dto.cid, 'pat456')

    def test_to_dict(self):
        kwargs = {
            '_id': '456',
            'username': 'patient_user',
            'password': 'patient_pass',
            'email': 'patient@example.com',
            'first_name': 'Patient',
            'last_name': 'User',
            'amka': '1234567890',
            'date_of_birth': '2000-01-01',
            'cid': 'pat456'
        }
        dto = PatientDto(**kwargs)
        expected_dict = {
            'cid': 'pat456',
            'username': 'patient_user',
            'email': 'patient@example.com',
            'first_name': 'Patient',
            'last_name': 'User',
            'amka': '1234567890',
            'date_of_birth': '2000-01-01'
        }
        self.assertEqual(dto.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
