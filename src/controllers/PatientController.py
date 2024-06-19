from flask import Blueprint, request

from src.entities.Patient import Patient
from src.entities.ResponseEntity import ResponseEntity
from src.entities.User import User
from src.services.PatientService import PatientService
from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto
from src.utils.Decorators import token_required, remove_token, handle_exceptions
from src.utils.EnvironmentConfig import Config
from src.utils.Http import HTTP
from src.utils.ResponseData import ResponseData

patient = Blueprint('patient', __name__)


@patient.route('/login', methods=['POST'])
@handle_exceptions
def login():
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(PatientService.login(User(**request.json)))
                       .resp_status(ResponseData.SUCCESS).build()).build())


@patient.route('/register', methods=['POST'])
@handle_exceptions
def register():
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(PatientService.register(Patient(**request.json)))
                       .resp_status(ResponseData.SUCCESS).build()).build())


@patient.route('/logout', methods=['GET'])
@remove_token(secret_key=Config.DOCTOR_SECRET_KEY)
@handle_exceptions
def logout(current_user):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(PatientService.logout(current_user))
                       .resp_status(ResponseData.SUCCESS).build()).build())


@patient.route('/book_appointment', methods=['POST'])
@token_required(secret_key=Config.PATIENT_SECRET_KEY)
@handle_exceptions
def book_appointment(current_user):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(PatientService.book_appointment(current_user, SearchAppointmentDto(**request.json)))
                       .resp_status(ResponseData.SUCCESS).build()).build())


@patient.route('/appointments', methods=['GET'])
@token_required(secret_key=Config.PATIENT_SECRET_KEY)
@handle_exceptions
def appointments(current_user):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(PatientService.fetch_appointments(current_user))
                       .resp_status(ResponseData.SUCCESS).build()).build())


@patient.route('/appointment/<appointment_id>', methods=['GET'])
@token_required(secret_key=Config.PATIENT_SECRET_KEY)
@handle_exceptions
def appointment_details(current_user, appointment_id):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data(PatientService.fetch_appointment_details(current_user, appointment_id))
                       .resp_status(ResponseData.SUCCESS).build()).build())


@patient.route('/cancel_appointment/<appointment_id>', methods=['DELETE'])
@token_required(secret_key=Config.PATIENT_SECRET_KEY)
@handle_exceptions
def cancel_appointment(current_user, appointment_id):
    return (ResponseEntity.builder()
            .with_status(HTTP.OK)
            .with_data(ResponseData.builder()
                       .resp_data({'Appointment canceled': PatientService.cancel_appointment(current_user,
                                                                                             appointment_id)})
                       .resp_status(ResponseData.SUCCESS).build()).build())
