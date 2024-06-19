import unittest
from unittest.mock import patch, MagicMock
from src.utils.SchemaValidator import SchemaValidator
from src.transfer.accept.ChangeAppointmentCostDto import ChangeAppointmentCostDto


class TestChangeAppointmentCostDto(unittest.TestCase):

    @patch.object(SchemaValidator, 'validate_appointment_cost')
    def test_initialization(self, mock_validate):
        mock_validate.return_value = None  # Mocking the validation function

        kwargs = {
            'username': 'test_user',
            'old_cost': 50,
            'new_cost': 75
        }

        dto = ChangeAppointmentCostDto(**kwargs)

        # Assertions
        self.assertEqual(dto.username, 'test_user')
        self.assertEqual(dto.old_cost, 50)
        self.assertEqual(dto.new_cost, 75)

    def test_to_dict(self):
        kwargs = {
            'username': 'test_user',
            'old_cost': 50,
            'new_cost': 75
        }
        dto = ChangeAppointmentCostDto(**kwargs)
        expected_dict = {
            'username': 'test_user',
            'old_cost': 50,
            'new_cost': 75
        }
        self.assertEqual(dto.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
