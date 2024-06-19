
from src.entities.Appointment import Appointment
from src.entities.Patient import Patient
from src.entities.User import User
from src.repositories.PatientRepository import PatientRepository
from src.services.AppointmentsService import AppointmentService
from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto
from src.transfer.send.DoctorDto import DoctorDto
from src.transfer.send.PatientAppointmentDto import PatientAppointmentDto
from src.transfer.send.PatientDetailedAppointmentDto import PatientDetailedAppointmentDto
from src.transfer.send.PatientDto import PatientDto
from src.transfer.send.UserDto import UserDto
from src.utils.AppointmentScheduler import AppointmentScheduler
from src.utils.DateUtils import DateTimeUtils
from src.utils.Http import HTTP
from src.utils.ServiceException import ServiceException
from src.utils.TokenFactory import JWT


class PatientService:

    @staticmethod
    def register(data: Patient):

        if PatientRepository.exists(data):
            raise ServiceException(
                str.format("Error during registration, Patient with username {} and email {} already exists",
                           data.username, data.email), HTTP.INTERNAL_SERVER_ERROR)

        patient = PatientRepository.register(data.to_db())
        if patient:
            return (UserDto(data.username,
                    JWT.generate_patient_token(User(**{"username": data.username, "password": data.password})))
                    .to_dict())

        raise ServiceException("Registration Error!", HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def login(auth_data: User):
        if PatientRepository.login(auth_data):
            return UserDto(auth_data.username, JWT.generate_patient_token(auth_data)).to_dict()

        raise ServiceException('Login failed! User not found!', HTTP.NOT_FOUND)

    @staticmethod
    def logout(token):
        if JWT.is_blacklisted(token):
            return True

        raise ServiceException('Logout failed', HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def book_appointment(current_user, data: SearchAppointmentDto):

        if not AppointmentService.check_time(DateTimeUtils.parse_time(data.appointment_time, '%H:%M')):
            raise ServiceException('Appointment time is outside working hours', HTTP.BAD_REQUEST)

        if not AppointmentService.check_date(data.appointment_date):
            raise ServiceException ('Appointment date is not available please select a date after today',HTTP.BAD_REQUEST)

        doctor: DoctorDto = AppointmentService.find_appointments(data)

        if not doctor:
            raise ServiceException("Not any available appointments found", HTTP.BAD_REQUEST)

        appointment_time = DateTimeUtils.parse_time(data.appointment_time, '%H:%M')
        appointment_date = DateTimeUtils.parse_date(data.appointment_date, '%Y-%m-%d')

        free_slots = AppointmentService.check_availability(doctor.username, appointment_date)

        if appointment_time not in free_slots:
            raise ServiceException('Appointment time is not available for selected date other free slots are available',
                                   HTTP.BAD_REQUEST)

        patient: PatientDto = PatientDto(**PatientRepository.find_by_username(current_user))

        appointment = Appointment.combined(doctor, patient, data)

        new_appointment = PatientRepository.book_appointment(appointment.to_dict())

        if new_appointment is None:
            raise ServiceException("Error booking appointment", HTTP.INTERNAL_SERVER_ERROR)

        return Appointment(**new_appointment).to_dict()

    @staticmethod
    def fetch_appointments(current_user):
        appointments = PatientRepository.fetch_appointments(current_user)
        if appointments:
            appointments_dto = PatientService.get_as_appointments(appointments)
            appointments_dto_list = []

            for appointment in appointments_dto:
                if AppointmentScheduler.is_date_within_rang(appointment.appointment_date):
                    appointments_dto_list.append(appointment.to_dict())
                return appointments_dto_list

        raise ServiceException('Error fetching appointments', HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def fetch_appointment_details(current_user, appointment_id):
        appointment = PatientRepository.fetch_appointment_details(current_user, appointment_id)
        if appointment:
            return PatientDetailedAppointmentDto(**appointment).to_dict()

        raise ServiceException("Error fetching patient appointment", HTTP.NOT_FOUND)

    @staticmethod
    def cancel_appointment(current_user, appointment_id):
        if PatientRepository.cancel_appointment(current_user, appointment_id):
            return True

        raise ServiceException("Error deleting patient", HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def get_as_appointments(appointments_dto):
        appointments = []
        for appointment in appointments_dto:
            appointments.append(PatientAppointmentDto(**appointment))
        return appointments
