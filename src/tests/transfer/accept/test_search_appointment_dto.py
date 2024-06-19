import unittest
from unittest.mock import patch, MagicMock
from src.utils.SchemaValidator import SchemaValidator
from src.transfer.accept.SearchAppointmentDto import SearchAppointmentDto


class TestSearchAppointmentDto(unittest.TestCase):

    @patch.object(SchemaValidator, 'validate_appointment_search')
    def test_initialization(self, mock_validate):
        mock_validate.return_value = None  # Mocking the validation function

        kwargs = {
            'reason': 'regular checkup',
            'specialization': 'Cardiologist',
            'appointment_date': '2024-06-20',
            'appointment_time': '10:00'
        }

        dto = SearchAppointmentDto(**kwargs)

        # Assertions
        self.assertEqual(dto.reason, 'regular checkup')
        self.assertEqual(dto.specialization, 'Cardiologist')
        self.assertEqual(dto.appointment_date, '2024-06-20')
        self.assertEqual(dto.appointment_time, '10:00')

    def test_to_dict(self):
        kwargs = {
            'reason': 'regular checkup',
            'specialization': 'Cardiologist',
            'appointment_date': '2024-06-20',
            'appointment_time': '10:00'
        }
        dto = SearchAppointmentDto(**kwargs)
        expected_dict = {
            'reason': 'regular checkup',
            'specialization': 'Cardiologist',
            'appointment_date': '2024-06-20',
            'appointment_time': '10:00'
        }
        self.assertEqual(dto.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
