from src.utils.SchemaValidator import SchemaValidator


class User:
    def __init__(self, **kwargs):
        SchemaValidator.validate_login(kwargs)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
        }

    def validate(self):
        return SchemaValidator.validate_login(self.to_dict())
