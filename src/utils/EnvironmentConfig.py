from enum import Enum


class Config(Enum):
    ADMIN_SECRET_KEY = 'admin_secret_key'
    DOCTOR_SECRET_KEY = 'doctor_secret_key'
    PATIENT_SECRET_KEY = 'patient_secret_key'
    URI = 'mongodb://localhost:27017/'
    HOST = 'mongodb'
    PORT = 27017
    DB = 'DigitalHospital'

    ADMIN_COLLECTION = 'admin'
    DOCTOR_COLLECTION = 'doctors'
    PATIENT_COLLECTION = 'patients'
    APPOINTMENT_COLLECTION = 'appointments'
