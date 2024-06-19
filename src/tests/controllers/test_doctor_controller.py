import json
import unittest
from unittest.mock import patch

from flask import Flask

from src.controllers.DoctorController import doctor
from src.utils.Http import HTTP


class TestDoctorController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(doctor)
        self.client = self.app.test_client()

    @patch('src.services.DoctorService.DoctorService.logout')
    def test_logout(self, MockLogout):
        # Mock data
        MockLogout.return_value = True

        # Make request
        response = self.client.get('/logout', headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertTrue(json.loads(response.data)['data']['Doctor Logged out'])

    @patch('src.services.DoctorService.DoctorService.login')
    def test_login(self, MockLogin):
        # Mock data
        MockLogin.return_value = {'username': 'test_doctor', 'token': 'mock_token'}

        # Make request
        response = self.client.post('/login', json={'username': 'test_doctor', 'password': 'test_password'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertEqual(json.loads(response.data)['data']['username'], 'test_doctor')
        self.assertEqual(json.loads(response.data)['data']['token'], 'mock_token')

    @patch('src.services.DoctorService.DoctorService.update_password')
    def test_update_password(self, MockUpdatePassword):
        # Mock data
        MockUpdatePassword.return_value = True

        # Make request
        response = self.client.put('/update_password',
                                   json={'current_password': 'old_pass', 'new_password': 'new_pass'},
                                   headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertTrue(json.loads(response.data)['data']['Password Changed'])

    @patch('src.services.DoctorService.DoctorService.update_appointment_cost')
    def test_update_appointment_cost(self, MockUpdateAppointmentCost):
        # Mock data
        MockUpdateAppointmentCost.return_value = True

        # Make request
        response = self.client.put('/update_appointment_cost', json={'new_cost': 150},
                                   headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertTrue(json.loads(response.data)['data']['Appointment cost updated'])

    @patch('src.services.DoctorService.DoctorService.fetch_appointments')
    def test_fetch_appointments(self, MockFetchAppointments):
        # Mock data
        MockFetchAppointments.return_value = [{'appointment_id': 1, 'appointment_date': '2024-07-01'}]

        # Make request
        response = self.client.get('/appointments', headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertEqual(len(json.loads(response.data)['data']), 1)
        self.assertEqual(json.loads(response.data)['data'][0]['appointment_id'], 1)
        self.assertEqual(json.loads(response.data)['data'][0]['appointment_date'], '2024-07-01')


if __name__ == '__main__':
    unittest.main()
