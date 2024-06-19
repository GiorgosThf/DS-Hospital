from flask import Blueprint, request

from src.entities.Doctor import Doctor
from src.entities.ResponseEntity import ResponseEntity
from src.entities.User import User
from src.services.AdminService import AdminService
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto
from src.utils.Decorators import token_required, remove_token, handle_exceptions
from src.utils.EnvironmentConfig import Config
from src.utils.Http import HTTP
from src.utils.ResponseData import ResponseData

admin = Blueprint('admin', __name__)


@admin.route('/login', methods=['POST'])
@handle_exceptions
def login():
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(AdminService.login(User(**request.json)))
                       .resp_status(ResponseData.SUCCESS).build())
            .build())


@admin.route('/logout', methods=['GET'])
@remove_token(secret_key=Config.ADMIN_SECRET_KEY)
@handle_exceptions
def logout(token):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data({'Admin Logged Out': AdminService.logout(token)})
                       .resp_status(ResponseData.SUCCESS).build())
            .build())


@admin.route('/create_doctor', methods=['POST'])
@token_required(secret_key=Config.ADMIN_SECRET_KEY)
@handle_exceptions
def create_doctor(current_user):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(AdminService.create_doctor(Doctor(**request.json)))
                       .resp_status(ResponseData.SUCCESS).build())
            .build())


@admin.route('/update_doctor_password', methods=['PUT'])
@token_required(secret_key=Config.ADMIN_SECRET_KEY)
@handle_exceptions
def update_doctor_password(current_user):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(
                        {'Password changed': AdminService.update_doctor_password(ChangePasswordDto(**request.json))})
                       .resp_status(ResponseData.SUCCESS).build())
            .build())


@admin.route('/delete_doctor/<username>', methods=['DELETE'])
@token_required(secret_key=Config.ADMIN_SECRET_KEY)
@handle_exceptions
def delete_doctor(current_user, username):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data({'Doctor deleted': AdminService.delete_doctor(username)})
                       .resp_status(ResponseData.SUCCESS).build())
            .build())


@admin.route('/delete_patient/<username>', methods=['DELETE'])
@token_required(secret_key=Config.ADMIN_SECRET_KEY)
@handle_exceptions
def delete_patient(current_user, username):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data({'Patient deleted': AdminService.delete_patient(username)})
                       .resp_status(ResponseData.SUCCESS).build())
            .build())
