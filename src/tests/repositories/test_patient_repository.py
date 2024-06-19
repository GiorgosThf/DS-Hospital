import unittest
from unittest.mock import patch

from bson import ObjectId

from src.entities.Appointment import Appointment
from src.entities.Patient import Patient
from src.entities.User import User
from src.repositories.PatientRepository import PatientRepository


class TestPatientRepository(unittest.TestCase):

    @patch('src.repositories.PatientRepository.PATIENT_COLLECTION')
    def test_register(self, mock_patient_collection):
        mock_patient_id = ObjectId('6170516e3171e9d4e1234567')
        mock_patient = {'_id': mock_patient_id, 'username': 'patient1'}
        mock_patient_collection.insert_one.return_value.inserted_id = mock_patient_id
        mock_patient_collection.find_one.return_value = mock_patient

        data = {'username': 'patient1', 'password': 'password123', 'email': 'patient1@example.com'}
        result = PatientRepository.register(data)

        self.assertIsNotNone(result)
        self.assertEqual(result['_id'], mock_patient_id)
        self.assertEqual(result['username'], 'patient1')

    @patch('src.repositories.PatientRepository.PATIENT_COLLECTION')
    def test_login_success(self, mock_patient_collection):
        mock_patient = {'username': 'patient1', 'password': 'password123'}
        mock_patient_collection.find_one.return_value = mock_patient

        auth_data = User(username='patient1', password='password123')
        result = PatientRepository.login(auth_data)

        self.assertIsNotNone(result)
        self.assertEqual(result['username'], 'patient1')

    @patch('src.repositories.PatientRepository.PATIENT_COLLECTION')
    def test_login_failure(self, mock_patient_collection):
        mock_patient_collection.find_one.return_value = None

        auth_data = User(username='patient1', password='password123')
        result = PatientRepository.login(auth_data)

        self.assertIsNone(result)

    @patch('src.repositories.PatientRepository.APPOINTMENT_COLLECTION')
    def test_book_appointment(self, mock_appointment_collection):
        mock_appointment_id = ObjectId('6170516e3171e9d4e1234567')
        mock_appointment = {'_id': mock_appointment_id, 'doctor_username': 'doctor1', 'patient_username': 'patient1'}
        mock_appointment_collection.insert_one.return_value.inserted_id = mock_appointment_id
        mock_appointment_collection.find_one.return_value = mock_appointment

        appointment_data = Appointment(_id=None, doctor_username='doctor1', patient_username='patient1',
                                       appointment_date='2023-06-18', appointment_time='10:00 AM',
                                       reason='Consultation', cost=100.0, specialization='Cardiology',
                                       doctor_name='doctor', doctor_surname='doctor', cid='APT',
                                       patient_name='patient', patient_surname='patient')

        result = PatientRepository.book_appointment(appointment_data)

        self.assertIsNotNone(result)
        self.assertEqual(result['_id'], mock_appointment_id)
        self.assertEqual(result['doctor_username'], 'doctor1')

    @patch('src.repositories.PatientRepository.APPOINTMENT_COLLECTION')
    def test_fetch_appointments(self, mock_appointment_collection):
        mock_appointments = [
            {'doctor_username': 'doctor1', 'patient_username': 'patient1', 'appointment_date': '2023-06-18'}]
        mock_appointment_collection.find.return_value = mock_appointments

        result = PatientRepository.fetch_appointments('patient1')

        self.assertEqual(result, mock_appointments)

    @patch('src.repositories.PatientRepository.APPOINTMENT_COLLECTION')
    def test_fetch_appointment_details(self, mock_appointment_collection):
        mock_appointment_id = ObjectId('6170516e3171e9d4e1234567')
        mock_appointment = {'_id': mock_appointment_id, 'doctor_username': 'doctor1', 'patient_username': 'patient1'}
        mock_appointment_collection.find_one.return_value = mock_appointment

        result = PatientRepository.fetch_appointment_details('patient1', mock_appointment_id)

        self.assertIsNotNone(result)
        self.assertEqual(result['_id'], mock_appointment_id)
        self.assertEqual(result['doctor_username'], 'doctor1')

    @patch('src.repositories.PatientRepository.APPOINTMENT_COLLECTION')
    def test_cancel_appointment(self, mock_appointment_collection):
        mock_appointment_collection.delete_one.return_value.deleted_count = 1

        result = PatientRepository.cancel_appointment('patient1', ObjectId('6170516e3171e9d4e1234567'))

        self.assertTrue(result)

    @patch('src.repositories.PatientRepository.PATIENT_COLLECTION')
    def test_find_by_username(self, mock_patient_collection):
        mock_patient = {'username': 'patient1', 'email': 'patient1@example.com'}
        mock_patient_collection.find_one.return_value = mock_patient

        result = PatientRepository.find_by_username('patient1')

        self.assertIsNotNone(result)
        self.assertEqual(result['username'], 'patient1')

    @patch('src.repositories.PatientRepository.PATIENT_COLLECTION')
    def test_exists(self, mock_patient_collection):
        mock_patient = {'username': 'patient1', 'email': 'patient1@example.com'}
        mock_patient_collection.find_one.return_value = mock_patient

        patient_data = Patient(username='patient1', password='password123', email='patient1@example.com',
                               first_name='Patient', last_name='One', amka='1234567890', date_of_birth='2000-01-01')
        result = PatientRepository.exists(patient_data)

        self.assertIsNotNone(result)
        self.assertEqual(result['username'], 'patient1')
        self.assertEqual(result['email'], 'patient1@example.com')


if __name__ == '__main__':
    unittest.main()
