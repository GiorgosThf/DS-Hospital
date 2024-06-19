from src.utils.SchemaValidator import SchemaValidator


class ChangePasswordDto:
    def __init__(self, **kwargs):
        SchemaValidator.validate_password(kwargs)
        self.username = kwargs.get('username', None)
        self.old_password = kwargs.get('old_password', None)
        self.new_password = kwargs.get('new_password', None)

    def to_dict(self):
        return {
            'username': self.username,
            'old_password': self.old_password,
            'new_password': self.new_password,
        }

