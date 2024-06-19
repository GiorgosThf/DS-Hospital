from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto
from src.transfer.send.DoctorDto import DoctorDto
from src.transfer.send.PatientDto import PatientDto
from src.utils.SchemaValidator import SchemaValidator


class Appointment:
    def __init__(self, _id, doctor_username, patient_username, patient_name, patient_surname, doctor_name,
                 doctor_surname, appointment_date, appointment_time, reason, cost, specialization,cid):
        self._id = _id
        self.cid = cid
        self.doctor_username = doctor_username
        self.patient_username = patient_username
        self.patient_name = patient_name
        self.patient_surname = patient_surname
        self.doctor_name = doctor_name
        self.doctor_surname = doctor_surname
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.reason = reason
        self.cost = cost
        self.specialization = specialization

    @classmethod
    def combined(cls, doctor: DoctorDto, patient: PatientDto, search: SearchAppointmentDto):
        _id = None
        cid = SchemaValidator.id_generator('APT', 7)
        return cls(_id, doctor.username, patient.username, patient.first_name, patient.last_name, doctor.first_name,
                   doctor.last_name, search.appointment_date, search.appointment_time, search.reason,
                   doctor.appointment_cost, doctor.specialization, cid)

    def to_dict(self):
        return {
            'cid': self.cid,
            'doctor_username': self.doctor_username,
            'patient_username': self.patient_username,
            'patient_name': self.patient_name,
            'patient_surname': self.patient_surname,
            'doctor_name': self.doctor_name,
            'doctor_surname': self.doctor_surname,
            'appointment_date': self.appointment_date,
            'appointment_time': self.appointment_time,
            'reason': self.reason,
            'cost': self.cost,
            'specialization': self.specialization,
        }
