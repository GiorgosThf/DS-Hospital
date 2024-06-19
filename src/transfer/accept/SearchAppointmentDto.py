from src.utils.SchemaValidator import SchemaValidator


class SearchAppointmentDto:
    def __init__(self, **kwargs):
        SchemaValidator.validate_appointment_search(kwargs)
        self.reason = kwargs.get('reason', None)
        self.specialization = kwargs.get('specialization', None)
        self.appointment_date = kwargs.get('appointment_date', None)
        self.appointment_time = kwargs.get('appointment_time', None)

    def to_dict(self):
        return {
            'reason': self.reason,
            'specialization': self.specialization,
            'appointment_time': self.appointment_time,
            'appointment_date': self.appointment_date,
        }

