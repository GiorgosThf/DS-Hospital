from src.utils.SchemaValidator import SchemaValidator


class Patient:
    def __init__(self, **kwargs):
        SchemaValidator.validate_patient_registration(kwargs)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.email = kwargs.get('email', None)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.amka = kwargs.get('amka', None)
        self.date_of_birth = kwargs.get('date_of_birth', None)

    def to_db(self):
        return {
            'cid': SchemaValidator.id_generator('DOC', 7),
            'username': self.username,
            "password": self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'amka': self.amka,
            'date_of_birth': self.date_of_birth
        }

    def to_register(self):
        return {
            'username': self.username,
            "password": self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'amka': self.amka,
            'date_of_birth': self.date_of_birth
        }

    def validate(self):
        return SchemaValidator.validate_patient_registration(self.to_register())
