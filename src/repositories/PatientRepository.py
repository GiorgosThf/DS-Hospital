from bson import ObjectId

from src.entities.Patient import Patient
from src.entities.User import User
from src.utils.EnvironmentConfig import Config
from src.utils.MongoDBConnection import MongoDBConnection

mongo = MongoDBConnection().connect()
PATIENT_COLLECTION = mongo[Config.PATIENT_COLLECTION.value]
APPOINTMENT_COLLECTION = mongo[Config.APPOINTMENT_COLLECTION.value]


class PatientRepository:

    @staticmethod
    def register(data):
        patient = PATIENT_COLLECTION.insert_one(data).inserted_id
        if patient is not None:
            return PATIENT_COLLECTION.find_one({'_id': ObjectId(patient)})
        return None

    @staticmethod
    def login(auth_data: User):
        patient = PATIENT_COLLECTION.find_one({"username": auth_data.username})
        if patient and patient['password'] == auth_data.password:
            return patient
        return None

    @staticmethod
    def book_appointment(appointment):
        appointment = APPOINTMENT_COLLECTION.insert_one(appointment).inserted_id
        if appointment is not None:
            return APPOINTMENT_COLLECTION.find_one({'_id': ObjectId(appointment)})
        return None

    @staticmethod
    def fetch_appointments(patient_username):
        return list(APPOINTMENT_COLLECTION.find({"patient_username": patient_username}))

    @staticmethod
    def fetch_appointment_details(username, appointment_id):
        return APPOINTMENT_COLLECTION.find_one({'cid': appointment_id, 'patient_username': username})

    @staticmethod
    def cancel_appointment(current_user, appointment_id):
        return (APPOINTMENT_COLLECTION
                .delete_one({'cid': appointment_id, 'patient_username': current_user})
                .deleted_count.real > 0)

    @staticmethod
    def find_by_username(username):
        return PATIENT_COLLECTION.find_one({'username': username})

    @staticmethod
    def exists(data: Patient):
        return PATIENT_COLLECTION.find_one({'$or': [{'username': data.username}, {'email': data.email}]})


