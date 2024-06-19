import unittest

from src.entities.Patient import Patient


class TestPatient(unittest.TestCase):

    def setUp(self):
        self.sample_patient_data = {
            'username': 'john_doe',
            'password': 'password123',
            'email': 'john.doe@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'amka': '1234567890',
            'date_of_birth': '1990-01-01'
        }

    def test_patient_initialization(self):
        patient = Patient(**self.sample_patient_data)

        assert patient.username == self.sample_patient_data['username']
        assert patient.password == self.sample_patient_data['password']
        assert patient.email == self.sample_patient_data['email']
        assert patient.first_name == self.sample_patient_data['first_name']
        assert patient.last_name == self.sample_patient_data['last_name']
        assert patient.amka == self.sample_patient_data['amka']
        assert patient.date_of_birth == self.sample_patient_data['date_of_birth']

    def test_patient_to_db(self):
        patient = Patient(**self.sample_patient_data)
        patient_dict = patient.to_db()

        self.assertEqual(patient_dict['username'], self.sample_patient_data['username'])
        assert patient_dict['password'] == self.sample_patient_data['password']
        assert patient_dict['email'] == self.sample_patient_data['email']
        assert patient_dict['first_name'] == self.sample_patient_data['first_name']
        assert patient_dict['last_name'] == self.sample_patient_data['last_name']
        assert patient_dict['amka'] == self.sample_patient_data['amka']
        assert patient_dict['date_of_birth'] == self.sample_patient_data['date_of_birth']

    def test_patient_to_register(self):
        patient = Patient(**self.sample_patient_data)
        register_dict = patient.to_register()

        assert register_dict['username'] == self.sample_patient_data['username']
        assert register_dict['password'] == self.sample_patient_data['password']
        assert register_dict['email'] == self.sample_patient_data['email']
        assert register_dict['first_name'] == self.sample_patient_data['first_name']
        assert register_dict['last_name'] == self.sample_patient_data['last_name']
        assert register_dict['amka'] == self.sample_patient_data['amka']
        assert register_dict['date_of_birth'] == self.sample_patient_data['date_of_birth']


if __name__ == '__main__':
    unittest.main()
