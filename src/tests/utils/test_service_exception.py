import unittest

from src.utils.Http import HTTP
from src.utils.ServiceException import DatabaseException
from src.utils.ServiceException import SchemaException
from src.utils.ServiceException import ServiceException


class TestCustomExceptions(unittest.TestCase):

    def test_service_exception(self):
        message = "Service error occurred"
        status_code = HTTP.BAD_REQUEST
        exception = ServiceException(message, status_code)

        self.assertEqual(exception.message, message)
        self.assertEqual(exception.status_code, status_code)
        self.assertIsInstance(exception, ServiceException)
        self.assertTrue(issubclass(ServiceException, Exception))

    def test_database_exception(self):
        message = "Database error occurred"
        status_code = HTTP.INTERNAL_SERVER_ERROR
        exception = DatabaseException(message, status_code)

        self.assertEqual(exception.message, message)
        self.assertEqual(exception.status_code, status_code)
        self.assertIsInstance(exception, DatabaseException)
        self.assertTrue(issubclass(DatabaseException, Exception))

    def test_schema_exception(self):
        message = "Schema validation error occurred"
        status_code = HTTP.INTERNAL_SERVER_ERROR
        exception = SchemaException(message, status_code)

        self.assertEqual(exception.message, message)
        self.assertEqual(exception.status_code, status_code)
        self.assertIsInstance(exception, SchemaException)
        self.assertTrue(issubclass(SchemaException, Exception))

    def test_service_exception_default_status_code(self):
        message = "Service error occurred"
        exception = ServiceException(message)

        self.assertEqual(exception.message, message)
        self.assertEqual(exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    def test_database_exception_default_status_code(self):
        message = "Database error occurred"
        exception = DatabaseException(message)

        self.assertEqual(exception.message, message)
        self.assertEqual(exception.status_code, HTTP.INTERNAL_SERVER_ERROR)

    def test_schema_exception_default_status_code(self):
        message = "Schema validation error occurred"
        exception = SchemaException(message)

        self.assertEqual(exception.message, message)
        self.assertEqual(exception.status_code, HTTP.INTERNAL_SERVER_ERROR)


if __name__ == '__main__':
    unittest.main()
