import pytest

from src.entities.User import User


@pytest.fixture
def sample_user_data():
    return {
        'username': 'user1',
        'password': 'password123'
    }


def test_user_initialization(sample_user_data):
    user = User(**sample_user_data)

    assert user.username == sample_user_data['username']
    assert user.password == sample_user_data['password']


def test_user_to_dict(sample_user_data):
    user = User(**sample_user_data)
    user_dict = user.to_dict()

    assert user_dict['username'] == sample_user_data['username']
    assert user_dict['password'] == sample_user_data['password']

