from src.entities.Doctor import Doctor
from src.entities.User import User
from src.repositories.AdminRepository import AdminRepository
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto
from src.transfer.send.DoctorDto import DoctorDto
from src.transfer.send.UserDto import UserDto
from src.utils.Http import HTTP
from src.utils.ServiceException import ServiceException
from src.utils.TokenFactory import JWT


class AdminService:

    @staticmethod
    def login(auth_data: User):
        if AdminRepository.login(auth_data):
            return UserDto(auth_data.username, JWT.generate_admin_token(auth_data)).to_dict()

        raise ServiceException('Login failed! User not found!', HTTP.NOT_FOUND)

    @staticmethod
    def logout(token):
        if JWT.is_blacklisted(token):
            return True

        raise ServiceException('Logout failed', HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def delete_doctor(username):
        if AdminRepository.delete_doctor(username):
            return True

        raise ServiceException("Error deleting doctor", HTTP.NOT_FOUND)

    @staticmethod
    def update_doctor_password(data: ChangePasswordDto):
        if AdminRepository.update_doctor_password(data):
            return True

        raise ServiceException("Error updating doctor password", HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def create_doctor(data: Doctor):
        if AdminRepository.doctor_exists(data):
            raise ServiceException(str.format(
                "Error creating doctor, Doctor with username {} and email {} already exists",
                data.username, data.email), HTTP.INTERNAL_SERVER_ERROR)

        doctor_new = AdminRepository.create_doctor(data.to_db())

        if doctor_new:
            return DoctorDto(**doctor_new).to_dict()

        raise ServiceException("Error creating doctor", HTTP.INTERNAL_SERVER_ERROR)

    @staticmethod
    def delete_patient(username):
        if AdminRepository.delete_patient(username):
            return True

        raise ServiceException("Error deleting patient", HTTP.INTERNAL_SERVER_ERROR)

