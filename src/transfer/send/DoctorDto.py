class DoctorDto:
    def __init__(self, _id=None, username=None, password=None, email=None, first_name=None, last_name=None,
                 specialization=None, appointment_cost=None, cid=None):
        self._id = str(_id) or None
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization
        self.appointment_cost = appointment_cost
        self.cid = cid

    def to_dict(self):
        return {
            'cid': self.cid,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'specialization': self.specialization,
            'appointment_cost': self.appointment_cost
        }
