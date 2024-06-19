import unittest
from src.transfer.send.UserDto import UserDto


class TestUserDto(unittest.TestCase):

    def test_initialization(self):
        kwargs = {
            'username': 'test_user',
            'token': 'abc123xyz'
        }

        dto = UserDto(**kwargs)

        # Assertions
        self.assertEqual(dto.username, 'test_user')
        self.assertEqual(dto.token, 'abc123xyz')

    def test_to_dict(self):
        kwargs = {
            'username': 'test_user',
            'token': 'abc123xyz'
        }
        dto = UserDto(**kwargs)
        expected_dict = {
            'username': 'test_user',
            'token': 'abc123xyz'
        }
        self.assertEqual(dto.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
