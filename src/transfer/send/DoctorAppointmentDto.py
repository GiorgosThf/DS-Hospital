class DoctorAppointmentDto:
    def __init__(self, **kwargs):
        self.cid = kwargs.get('cid')
        self.patient_name = kwargs.get('patient_name')
        self.patient_surname = kwargs.get('patient_surname')
        self.appointment_date = kwargs.get('appointment_date')
        self.appointment_time = kwargs.get('appointment_time')
        self.reason = kwargs.get('reason')

    def to_dict(self):
        return {
            'cid': self.cid,
            'patient_name': self.patient_name,
            'patient_surname': self.patient_surname,
            'appointment_time': self.appointment_time,
            'appointment_date': self.appointment_date,
            'reason': self.reason,
        }
