import json
import unittest
from unittest.mock import patch

import allure
from flask import Flask

from src.controllers import AdminController
from src.utils.Http import HTTP

allure.feature('Admin Controller')


class TestAdminController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(AdminController.admin)
        self.client = self.app.test_client()

    @patch('src.services.AdminService.AdminService.login')
    def test_login(self, MockLogin):
        # Mock data
        MockLogin.return_value = {'username': 'admin_user', 'token': 'mock_token'}

        # Make request
        response = self.client.post('/login', json={'username': 'admin_user', 'password': 'admin_password'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertEqual(json.loads(response.data)['data']['username'], 'admin_user')
        self.assertEqual(json.loads(response.data)['data']['token'], 'mock_token')

    @patch('src.services.AdminService.AdminService.logout')
    def test_logout(self, MockLogout):
        # Mock data
        MockLogout.return_value = True

        # Make request
        response = self.client.get('/logout', headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertTrue(json.loads(response.data)['data']['Admin Logged Out'])

    @patch('src.services.AdminService.AdminService.create_doctor')
    def test_create_doctor(self, MockCreateDoctor):
        # Mock data
        MockCreateDoctor.return_value = {'username': 'new_doctor', 'email': 'doctor@example.com'}

        # Make request
        response = self.client.post('/create_doctor', json={'username': 'new_doctor', 'email': 'doctor@example.com',
                                                            'password': 'password'},
                                    headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'SUCCESS')
        self.assertEqual(json.loads(response.data)['data']['username'], 'new_doctor')
        self.assertEqual(json.loads(response.data)['data']['email'], 'doctor@example.com')

    @patch('src.services.AdminService.AdminService.update_doctor_password')
    def test_update_doctor_password(self, MockUpdateDoctorPassword):
        # Mock data
        MockUpdateDoctorPassword.return_value = True

        # Make request
        response = self.client.put('/update_doctor_password',
                                   json={'username': 'doctor1', 'old_password': 'old_password',
                                         'new_password': 'new_password'},
                                   headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertTrue(json.loads(response.data)['data']['Password changed'])

    @patch('src.services.AdminService.AdminService.delete_doctor')
    def test_delete_doctor(self, MockDeleteDoctor):
        # Mock data
        MockDeleteDoctor.return_value = True

        # Make request
        response = self.client.delete('/delete_doctor/doctor1', headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertTrue(json.loads(response.data)['data']['Doctor deleted'])

    @patch('src.services.AdminService.AdminService.delete_patient')
    def test_delete_patient(self, MockDeletePatient):
        # Mock data
        MockDeletePatient.return_value = True

        # Make request
        response = self.client.delete('/delete_patient/patient1', headers={'Authorization': 'Bearer mock_token'})

        # Assertions
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertEqual(json.loads(response.data)['status'], 'success')
        self.assertTrue(json.loads(response.data)['data']['Patient deleted'])


if __name__ == '__main__':
    unittest.main()
