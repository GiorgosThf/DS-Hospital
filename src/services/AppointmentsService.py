
from src.repositories.DoctorRepository import DoctorRepository
from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto
from src.transfer.send.DoctorDto import DoctorDto
from src.utils.AppointmentScheduler import AppointmentScheduler
from src.utils.DateUtils import DateTimeUtils


class AppointmentService:

    @staticmethod
    def check_time(appointment_time):
        return AppointmentScheduler.is_within_working_hours(appointment_time)

    @staticmethod
    def check_date(appointment_date):
        return AppointmentScheduler.is_date_within_rang(appointment_date)

    @staticmethod
    def check_availability(doctor_username, appointment_date):

        appointments = (DoctorRepository
                        .fetch_appointments_by_date(doctor_username,
                                                    DateTimeUtils.date_to_string(appointment_date, '%Y-%m-%d')))

        available_slots = AppointmentScheduler.create_appointment_slots()

        booked_slots = [DateTimeUtils.parse_time(appt['appointment_time'], '%H:%M') for appt in appointments]

        free_slots = [slot for slot in available_slots if slot not in booked_slots]

        return free_slots

    @staticmethod
    def find_appointments(data: SearchAppointmentDto):
        appointment_time = DateTimeUtils.parse_time(data.appointment_time,'%H:%M')
        appointment_date = DateTimeUtils.parse_date(data.appointment_date, '%Y-%m-%d')

        doctors = AppointmentService.return_doctors(DoctorRepository.find_by_role(data))

        for doctor in doctors:
            free_appointments = AppointmentService.check_availability(doctor.username, appointment_date)
            if appointment_time in free_appointments:
                return doctor
            break

        return None

    @staticmethod
    def return_appointments(free_appointments):
        slots = []
        for slot in free_appointments:
            slots.append(DateTimeUtils.time_to_string(slot, '%H:%M'))
        return slots

    @staticmethod
    def return_doctors(doctors):
        docs = []
        for doc in doctors:
            docs.append(DoctorDto(**doc))
        return docs
