import unittest

from src.entities.Appointment import Appointment
from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto
from src.transfer.send.DoctorDto import DoctorDto
from src.transfer.send.PatientDto import PatientDto


class TestAppointment(unittest.TestCase):

    def setUp(self):
        self.sample_doctor = DoctorDto(username='dr_smith', first_name='John', last_name='Smith', appointment_cost=100,
                                       specialization='Cardiologist')
        self.sample_patient = PatientDto(username='patient_jane', first_name='Jane', last_name='Doe')
        self.sample_search = SearchAppointmentDto(appointment_date='2024-07-01', appointment_time='10:00',
                                                  reason='Regular checkup', specialization='Cardiologist')

    def test_appointment_initialization(self):
        appointment = Appointment.combined(self.sample_doctor, self.sample_patient, self.sample_search)

        self.assertEqual(appointment.doctor_username, self.sample_doctor.username)
        self.assertEqual(appointment.patient_username, self.sample_patient.username)
        self.assertEqual(appointment.patient_name, self.sample_patient.first_name)
        self.assertEqual(appointment.patient_surname, self.sample_patient.last_name)
        self.assertEqual(appointment.doctor_name, self.sample_doctor.first_name)
        self.assertEqual(appointment.doctor_surname, self.sample_doctor.last_name)
        self.assertEqual(appointment.appointment_date, self.sample_search.appointment_date)
        self.assertEqual(appointment.appointment_time, self.sample_search.appointment_time)
        self.assertEqual(appointment.reason, self.sample_search.reason)
        self.assertEqual(appointment.cost, self.sample_doctor.appointment_cost)
        self.assertEqual(appointment.specialization, self.sample_doctor.specialization)
        self.assertTrue(appointment.cid.startswith('APT'))  # Assuming cid is generated correctly

    def test_appointment_to_dict(self):
        appointment = Appointment.combined(self.sample_doctor, self.sample_patient, self.sample_search)
        appointment_dict = appointment.to_dict()

        self.assertEqual(appointment_dict['doctor_username'], self.sample_doctor.username)
        self.assertEqual(appointment_dict['patient_username'], self.sample_patient.username)
        self.assertEqual(appointment_dict['patient_name'], self.sample_patient.first_name)
        self.assertEqual(appointment_dict['patient_surname'], self.sample_patient.last_name)
        self.assertEqual(appointment_dict['doctor_name'], self.sample_doctor.first_name)
        self.assertEqual(appointment_dict['doctor_surname'], self.sample_doctor.last_name)
        self.assertEqual(appointment_dict['appointment_date'], self.sample_search.appointment_date)
        self.assertEqual(appointment_dict['appointment_time'], self.sample_search.appointment_time)
        self.assertEqual(appointment_dict['reason'], self.sample_search.reason)
        self.assertEqual(appointment_dict['cost'], self.sample_doctor.appointment_cost)
        self.assertEqual(appointment_dict['specialization'], self.sample_doctor.specialization)
        self.assertTrue(appointment_dict['cid'].startswith('APT'))  # Assuming cid is included correctly


if __name__ == '__main__':
    unittest.main()
