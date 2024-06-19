class UserDto:
    def __init__(self, username,  token):
        self.username = username
        self.token = token

    def to_dict(self):
        return {
            'username': self.username,
            'token': self.token,
        }
