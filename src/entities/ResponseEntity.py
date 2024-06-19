import json

from flask import Response


class ResponseEntity:
    def __init__(self):
        self.data = None,
        self.status = None
        self.mimetype = 'application/json'

    @staticmethod
    def builder():
        return ResponseEntityBuilder()


class ResponseEntityBuilder:
    def __init__(self):
        self.response = ResponseEntity()

    def with_status(self, status):
        self.response.status = status
        return self

    def with_data(self, data):
        self.response.data = data
        return self

    def with_content_type(self, content_type):
        self.response.content_type = content_type
        return self

    def build(self):
        return Response(json.dumps(self.response.data), status=self.response.status, mimetype=self.response.mimetype)
