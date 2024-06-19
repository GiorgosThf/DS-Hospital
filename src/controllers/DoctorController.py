from flask import Blueprint, request

from src.entities.ResponseEntity import ResponseEntity
from src.entities.User import User
from src.services.DoctorService import DoctorService
from src.transfer.accept.ChangeAppointmentCostDto import ChangeAppointmentCostDto
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto
from src.utils.Decorators import token_required, remove_token, handle_exceptions
from src.utils.EnvironmentConfig import Config
from src.utils.Http import HTTP
from src.utils.ResponseData import ResponseData

doctor = Blueprint('doctor', __name__)


@doctor.route('/logout', methods=['GET'])
@remove_token(secret_key=Config.DOCTOR_SECRET_KEY)
@handle_exceptions
def logout(current_user):
    return (ResponseEntity.builder().with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data({'Doctor Logged out': DoctorService.logout(current_user)})
                       .resp_status(ResponseData.SUCCESS).build()).build())


@doctor.route('/login', methods=['POST'])
@handle_exceptions
def login():
    return (ResponseEntity.builder().with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(DoctorService.login(User(**request.json)))
                       .resp_status(ResponseData.SUCCESS).build()).build())


@doctor.route('/update_password', methods=['PUT'])
@token_required(secret_key=Config.DOCTOR_SECRET_KEY)
@handle_exceptions
def update_password(current_user):
    return (ResponseEntity.builder().with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(
                        {'Password Changed': DoctorService.update_password(
                            current_user, ChangePasswordDto(**request.json))})
                       .resp_status(ResponseData.SUCCESS).build()).build())


@doctor.route('/update_appointment_cost', methods=['PUT'])
@token_required(secret_key=Config.DOCTOR_SECRET_KEY)
@handle_exceptions
def update_appointment_cost(current_user):
    return (ResponseEntity.builder().with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data({'Appointment cost updated': DoctorService.update_appointment_cost(
                        current_user, ChangeAppointmentCostDto(**request.json))})
                       .resp_status(ResponseData.SUCCESS)
                       .build()).build())


@doctor.route('/appointments', methods=['GET'])
@token_required(secret_key=Config.DOCTOR_SECRET_KEY)
@handle_exceptions
def appointments(current_user):
    return (ResponseEntity.builder().with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(DoctorService.fetch_appointments(current_user))
                       .resp_status(ResponseData.SUCCESS).build()).build())
