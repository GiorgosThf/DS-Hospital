from bson import ObjectId

from src.entities.Doctor import Doctor
from src.entities.User import User
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto
from src.utils.EnvironmentConfig import Config
from src.utils.MongoDBConnection import MongoDBConnection

mongo = MongoDBConnection().connect()
PATIENT_COLLECTION = mongo[Config.PATIENT_COLLECTION.value]
DOCTOR_COLLECTION = mongo[Config.DOCTOR_COLLECTION.value]
ADMIN_COLLECTION = mongo[Config.ADMIN_COLLECTION.value]


class AdminRepository:

    @staticmethod
    def login(auth_data: User):
        admin = ADMIN_COLLECTION.find_one({"username": auth_data.username})
        if admin and admin['password'] == auth_data.password:
            return admin
        return None

    @staticmethod
    def create_doctor(data):
        doctor = DOCTOR_COLLECTION.insert_one(data).inserted_id
        if doctor is not None:
            return DOCTOR_COLLECTION.find_one({'_id': ObjectId(doctor)})
        return None

    @staticmethod
    def delete_doctor(username):
        return DOCTOR_COLLECTION.delete_one({'username': username}).deleted_count.real > 0

    @staticmethod
    def update_doctor_password(data: ChangePasswordDto):

        doctor = DOCTOR_COLLECTION.find_one({"username": data.username})
        if doctor and doctor['password'] == data.old_password:
            return DOCTOR_COLLECTION.update_one({'username': data.username},
                                                {'$set': {'password': data.new_password}}).modified_count.real > 0
        return None

    @staticmethod
    def delete_patient(username):
        return PATIENT_COLLECTION.delete_one({'username': username}).deleted_count.real > 0

    @staticmethod
    def doctor_exists(data: Doctor):
        return DOCTOR_COLLECTION.find_one({'$or': [{'username': data.username}, {'email': data.email}]})
