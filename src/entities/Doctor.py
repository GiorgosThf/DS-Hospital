from src.utils.SchemaValidator import SchemaValidator


class Doctor:
    def __init__(self, **kwargs):
        SchemaValidator.validate_doctor_registration(kwargs)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.email = kwargs.get('email', None)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.specialization = kwargs.get('specialization', None)
        self.appointment_cost = kwargs.get('appointment_cost', None)

    def to_db(self):
        return {
            'cid': SchemaValidator.id_generator('DOC', 7),
            'username': self.username,
            "password": self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'specialization': self.specialization,
            'appointment_cost': self.appointment_cost
        }

    def to_register(self):
        return {
            'username': self.username,
            "password": self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'specialization': self.specialization,
            'appointment_cost': self.appointment_cost
        }
