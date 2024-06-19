import unittest

from src.utils.Http import HTTP


class TestHTTPStatus(unittest.TestCase):

    def test_http_status_codes(self):

        self.assertEqual(HTTP.OK, 200)
        self.assertEqual(HTTP.CREATED, 201)
        self.assertEqual(HTTP.ACCEPTED, 202)
        self.assertEqual(HTTP.NO_CONTENT, 204)

        self.assertEqual(HTTP.BAD_REQUEST, 400)
        self.assertEqual(HTTP.UNAUTHORIZED, 401)
        self.assertEqual(HTTP.FORBIDDEN, 403)
        self.assertEqual(HTTP.NOT_FOUND, 404)

        self.assertEqual(HTTP.INTERNAL_SERVER_ERROR, 500)
        self.assertEqual(HTTP.NOT_IMPLEMENTED, 501)
        self.assertEqual(HTTP.BAD_GATEWAY, 502)
        self.assertEqual(HTTP.SERVICE_UNAVAILABLE, 503)


if __name__ == '__main__':
    unittest.main()
