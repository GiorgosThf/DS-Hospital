from src.utils.Http import HTTP


class ServiceException(Exception):
    def __init__(self, message, status_code=HTTP.INTERNAL_SERVER_ERROR):
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class DatabaseException(Exception):
    def __init__(self, message, status_code=HTTP.INTERNAL_SERVER_ERROR):
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class SchemaException(Exception):
    def __init__(self, message, status_code=HTTP.INTERNAL_SERVER_ERROR):
        super().__init__(message)
        self.status_code = status_code
        self.message = message

