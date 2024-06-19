import json
import unittest
from unittest.mock import patch

from flask import Flask

from src.controllers.PatientController import patient
from src.utils.Http import HTTP


class TestPatientController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(patient)
        self.client = self.app.test_client()

    @patch('src.services.PatientService.PatientService.login')
    def test_login(self, MockLogin):
        # Mock data
        MockLogin.return_value = {'username': 'test_patient', 'token': 'mock_token'}

        # Make request
        response = self.client.post('/login', json={'username': 'test_patient', 'password': 'test_password'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertEqual(json.loads(response.data)['data']['username'], 'test_patient')
        self.assertEqual(json.loads(response.data)['data']['token'], 'mock_token')

    @patch('src.services.PatientService.PatientService.register')
    def test_register(self, MockRegister):
        # Mock data
        MockRegister.return_value = {'username': 'new_patient', 'token': 'new_mock_token'}

        # Make request
        response = self.client.post('/register', json={'username': 'new_patient', 'email': 'test@example.com',
                                                       'password': 'new_password'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'SUCCESS')
        self.assertEqual(json.loads(response.data)['data']['username'], 'new_patient')
        self.assertEqual(json.loads(response.data)['data']['token'], 'new_mock_token')

    @patch('src.services.PatientService.PatientService.logout')
    def test_logout(self, MockLogout):
        # Mock data
        MockLogout.return_value = True

        # Make request
        response = self.client.get('/logout', headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'SUCCESS')
        self.assertTrue(json.loads(response.data)['data'])

    @patch('src.services.PatientService.PatientService.book_appointment')
    def test_book_appointment(self, MockBookAppointment):
        # Mock data
        MockBookAppointment.return_value = {'appointment_id': 1, 'appointment_time': '10:00',
                                            'appointment_date': '2024-07-01'}

        # Make request
        response = self.client.post('/book_appointment',
                                    json={'doctor_username': 'doctor1', 'appointment_date': '2024-07-01',
                                          'appointment_time': '10:00'}, headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'SUCCESS')
        self.assertEqual(json.loads(response.data)['data']['appointment_id'], 1)

    @patch('src.services.PatientService.PatientService.fetch_appointments')
    def test_fetch_appointments(self, MockFetchAppointments):
        # Mock data
        MockFetchAppointments.return_value = [{'appointment_id': 1, 'appointment_date': '2024-07-01'}]

        # Make request
        response = self.client.get('/appointments', headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'SUCCESS')
        self.assertEqual(len(json.loads(response.data)['data']), 1)
        self.assertEqual(json.loads(response.data)['data'][0]['appointment_id'], 1)

    @patch('src.services.PatientService.PatientService.fetch_appointment_details')
    def test_fetch_appointment_details(self, MockFetchAppointmentDetails):
        # Mock data
        MockFetchAppointmentDetails.return_value = {'appointment_id': 1, 'appointment_date': '2024-07-01',
                                                    'details': 'Sample details'}

        # Make request
        response = self.client.get('/appointment/1', headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'SUCCESS')
        self.assertEqual(json.loads(response.data)['data']['appointment_id'], 1)
        self.assertEqual(json.loads(response.data)['data']['details'], 'Sample details')

    @patch('src.services.PatientService.PatientService.cancel_appointment')
    def test_cancel_appointment(self, MockCancelAppointment):
        # Mock data
        MockCancelAppointment.return_value = True

        # Make request
        response = self.client.delete('/cancel_appointment/1', headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'SUCCESS')
        self.assertTrue(json.loads(response.data)['data']['Appointment canceled'])


if __name__ == '__main__':
    unittest.main()
