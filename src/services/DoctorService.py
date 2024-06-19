from src.entities.User import User
from src.repositories.DoctorRepository import DoctorRepository
from src.transfer.accept.ChangeAppointmentCostDto import ChangeAppointmentCostDto
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto
from src.transfer.send.DoctorAppointmentDto import DoctorAppointmentDto
from src.transfer.send.UserDto import UserDto
from src.utils.AppointmentScheduler import AppointmentScheduler
from src.utils.Http import HTTP
from src.utils.ServiceException import ServiceException
from src.utils.TokenFactory import JWT


class DoctorService:

    @staticmethod
    def login(auth_data: User):
        if DoctorRepository.login(auth_data):
            return UserDto(auth_data.username, JWT.generate_doctor_token(auth_data)).to_dict()

        raise ServiceException('Login failed! User not found!', HTTP.NOT_FOUND)

    @staticmethod
    def logout(token):
        if JWT.is_blacklisted(token):
            return True

        raise ServiceException('Logout failed', HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def update_password(current_user, data: ChangePasswordDto):
        if DoctorRepository.update_password(current_user, data):
            return True

        raise ServiceException("Error updating password", HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def update_appointment_cost(current_user, data: ChangeAppointmentCostDto):
        if DoctorRepository.update_appointment_cost(current_user, data):
            return True

        raise ServiceException("Error updating appointment cost", HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def fetch_appointments(current_user):
        appointments = DoctorRepository.fetch_appointments(current_user)

        if appointments:
            appointments_dto = DoctorService.get_as_appointments(appointments)
            appointments_dto_list = []

            for appointment in appointments_dto:

                if AppointmentScheduler.is_date_within_rang(appointment.appointment_date):
                    appointments_dto_list.append(appointment.to_dict())

            return appointments_dto_list

        raise ServiceException('Error fetching appointments', HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def get_as_appointments(appointments_dto):
        appointments = []
        for appointment in appointments_dto:
            appointments.append(DoctorAppointmentDto(**appointment))
        return appointments
