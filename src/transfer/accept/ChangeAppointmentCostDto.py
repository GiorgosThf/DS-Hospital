from src.utils.SchemaValidator import SchemaValidator


class ChangeAppointmentCostDto:
    def __init__(self,  **kwargs):
        SchemaValidator.validate_appointment_cost(kwargs)
        self.username = kwargs.get('username', None)
        self.old_cost = kwargs.get('old_cost', None)
        self.new_cost = kwargs.get('new_cost', None)

    def to_dict(self):
        return {
            'username': self.username,
            'old_cost': self.old_cost,
            'new_cost': self.new_cost,
        }
