import unittest
from unittest.mock import patch, MagicMock
from src.utils.SchemaValidator import SchemaValidator
from src.transfer.accept.ChangePasswordDto import ChangePasswordDto


class TestChangePasswordDto(unittest.TestCase):

    @patch.object(SchemaValidator, 'validate_password')
    def test_initialization(self, mock_validate):
        mock_validate.return_value = None  # Mocking the validation function

        kwargs = {
            'username': 'test_user',
            'old_password': 'old_pass',
            'new_password': 'new_pass'
        }

        dto = ChangePasswordDto(**kwargs)

        # Assertions
        self.assertEqual(dto.username, 'test_user')
        self.assertEqual(dto.old_password, 'old_pass')
        self.assertEqual(dto.new_password, 'new_pass')

    def test_to_dict(self):
        kwargs = {
            'username': 'test_user',
            'old_password': 'old_pass',
            'new_password': 'new_pass'
        }
        dto = ChangePasswordDto(**kwargs)
        expected_dict = {
            'username': 'test_user',
            'old_password': 'old_pass',
            'new_password': 'new_pass'
        }
        self.assertEqual(dto.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
