from src.entities.User import User
from src.transfer.accept.ChangeAppointmentCostDto import ChangeAppointmentCostDto
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto
from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto
from src.utils.EnvironmentConfig import Config
from src.utils.MongoDBConnection import MongoDBConnection

mongo = MongoDBConnection().connect()
APPOINTMENT_COLLECTION = mongo[Config.APPOINTMENT_COLLECTION.value]
DOCTOR_COLLECTION = mongo[Config.DOCTOR_COLLECTION.value]


class DoctorRepository:

    @staticmethod
    def login(auth_data: User):
        doctor = DOCTOR_COLLECTION.find_one({"username": auth_data.username})
        if doctor and doctor['password'] == auth_data.password:
            return doctor
        return None

    @staticmethod
    def update_password(username, data: ChangePasswordDto):
        doctor = DOCTOR_COLLECTION.find_one({"username": username})

        if doctor and doctor['password'] == data.old_password and doctor['username'] == data.username:
            return DOCTOR_COLLECTION.update_one({'username': data.username},
                                                {'$set': {'password': data.new_password}}).modified_count.real > 0
        return None

    @staticmethod
    def update_appointment_cost(username, data: ChangeAppointmentCostDto):
        doctor = DOCTOR_COLLECTION.find_one({"username": username})

        if doctor and doctor['appointment_cost'] == data.old_cost and doctor['username'] == data.username:
            return DOCTOR_COLLECTION.update_one({"username": username},
                                                {"$set": {"appointment_cost": data.new_cost}}).modified_count.real > 0
        return None

    @staticmethod
    def fetch_appointments(doctor_username):
        return list(APPOINTMENT_COLLECTION.find({"doctor_username": doctor_username}))

    @staticmethod
    def fetch_appointments_by_date(doctor_username, appointment_date):
        return list(APPOINTMENT_COLLECTION.find({"doctor_username": doctor_username,
                                                 "appointment_date": appointment_date}))

    @staticmethod
    def find_by_role(data: SearchAppointmentDto):
        return list(DOCTOR_COLLECTION.find({"specialization": data.specialization}))
