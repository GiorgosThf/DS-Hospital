class PatientDto:
    def __init__(self, _id=None, username=None, password=None, email=None, first_name=None, last_name=None,
                 amka=None, date_of_birth=None, cid=None):
        self._id = str(_id) or None
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.amka = amka
        self.date_of_birth = date_of_birth
        self.cid = cid

    def to_dict(self):
        return {
            'cid': self.cid,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'amka': self.amka,
            'date_of_birth': self.date_of_birth
        }
