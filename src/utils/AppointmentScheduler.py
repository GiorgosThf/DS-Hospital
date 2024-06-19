from datetime import datetime, timedelta


class AppointmentScheduler:
    WORKING_HOURS_START = 9
    WORKING_HOURS_END = 17
    APPOINTMENT_DURATION = timedelta(hours=1)

    @staticmethod
    def is_within_working_hours(appointment_time):
        return (AppointmentScheduler.WORKING_HOURS_START <= appointment_time.hour
                < AppointmentScheduler.WORKING_HOURS_END)

    @staticmethod
    def is_date_within_rang(appointment_date):
        return datetime.strptime(appointment_date, '%Y-%m-%d').date() > datetime.now().date()

    @staticmethod
    def create_appointment_slots():
        slots = []
        current_time = datetime.strptime('09:00', '%H:%M')
        end_time = datetime.strptime('17:00', '%H:%M')

        while current_time < end_time:
            slots.append(current_time.time())
            current_time += AppointmentScheduler.APPOINTMENT_DURATION
        return slots
