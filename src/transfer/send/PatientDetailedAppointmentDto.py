class PatientDetailedAppointmentDto:
    def __init__(self, **kwargs):
        self.cid = kwargs.get('cid')
        self.doctor_name = kwargs.get('doctor_name',)
        self.doctor_surname = kwargs.get('doctor_surname',)
        self.appointment_date = kwargs.get('appointment_date')
        self.appointment_time = kwargs.get('appointment_time')
        self.specialization = kwargs.get('specialization')
        self.cost = kwargs.get('cost')
        self.reason = kwargs.get('reason')

    def to_dict(self):
        return {
            'cid': self.cid,
            'doctor_name': self.doctor_name,
            'doctor_surname': self.doctor_surname,
            'appointment_time': self.appointment_time,
            'appointment_date': self.appointment_date,
            'specialization': self.specialization,
            'cost': self.cost,
            'reason': self.reason
        }
