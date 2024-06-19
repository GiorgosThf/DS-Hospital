import unittest

from src.entities.Doctor import Doctor


class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.sample_doctor_data = {
            'username': 'dr_smith',
            'password': 'doctor123',
            'email': 'dr.smith@example.com',
            'first_name': 'John',
            'last_name': 'Smith',
            'specialization': 'Radiologist',
            'appointment_cost': 100.0
        }

    def test_doctor_initialization(self):
        doctor = Doctor(**self.sample_doctor_data)

        self.assertEqual(doctor.username, self.sample_doctor_data['username'])
        self.assertEqual(doctor.password, self.sample_doctor_data['password'])
        self.assertEqual(doctor.email, self.sample_doctor_data['email'])
        self.assertEqual(doctor.first_name, self.sample_doctor_data['first_name'])
        self.assertEqual(doctor.last_name, self.sample_doctor_data['last_name'])
        self.assertEqual(doctor.specialization, self.sample_doctor_data['specialization'])
        self.assertEqual(doctor.appointment_cost, self.sample_doctor_data['appointment_cost'])

    def test_doctor_to_db(self):
        doctor = Doctor(**self.sample_doctor_data)
        doctor_dict = doctor.to_db()

        self.assertEqual(doctor_dict['username'], self.sample_doctor_data['username'])
        self.assertEqual(doctor_dict['password'], self.sample_doctor_data['password'])
        self.assertEqual(doctor_dict['email'], self.sample_doctor_data['email'])
        self.assertEqual(doctor_dict['first_name'], self.sample_doctor_data['first_name'])
        self.assertEqual(doctor_dict['last_name'], self.sample_doctor_data['last_name'])
        self.assertEqual(doctor_dict['specialization'], self.sample_doctor_data['specialization'])
        self.assertEqual(doctor_dict['appointment_cost'], self.sample_doctor_data['appointment_cost'])

    def test_doctor_to_register(self):
        doctor = Doctor(**self.sample_doctor_data)
        register_dict = doctor.to_register()

        self.assertEqual(register_dict['username'], self.sample_doctor_data['username'])
        self.assertEqual(register_dict['password'], self.sample_doctor_data['password'])
        self.assertEqual(register_dict['email'], self.sample_doctor_data['email'])
        self.assertEqual(register_dict['first_name'], self.sample_doctor_data['first_name'])
        self.assertEqual(register_dict['last_name'], self.sample_doctor_data['last_name'])
        self.assertEqual(register_dict['specialization'], self.sample_doctor_data['specialization'])
        self.assertEqual(register_dict['appointment_cost'], self.sample_doctor_data['appointment_cost'])


if __name__ == '__main__':
    unittest.main()
