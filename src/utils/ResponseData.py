from datetime import datetime


class ResponseData:

    SUCCESS = 'success'
    ERROR = 'error'
    DEFAULT = 'message'

    def __init__(self):
        self.status = None
        self.error = None
        self.data = None

    @staticmethod
    def builder():
        return ResponseDataBuilder()


class ResponseDataBuilder:
    def __init__(self):
        self.response_data = ResponseData()

    def resp_status(self, status):
        self.response_data.status = status
        return self

    def error(self, error):
        self.response_data.error = error
        return self

    def resp_data(self, data):
        self.response_data.data = data
        return self

    def build(self):
        response_data = {}

        if self.response_data.status:
            response_data.setdefault('status', self.response_data.status)
        if self.response_data.error:
            response_data.setdefault('error', self.response_data.error)
        if self.response_data.data:
            response_data.setdefault('data', self.response_data.data)
        response_data.setdefault('date', str(datetime.now()))

        return response_data


