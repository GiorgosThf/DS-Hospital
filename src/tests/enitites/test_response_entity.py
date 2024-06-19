import json
import unittest

from flask import Response

from src.entities.ResponseEntity import ResponseEntity


class TestResponseEntity(unittest.TestCase):

    def test_response_entity_builder(self):
        builder = ResponseEntity.builder()
        response = builder.with_status(200).with_data({'message': 'Success'}).build()

        assert isinstance(response, Response)
        assert response.status_code == 200
        assert response.mimetype == 'application/json'
        assert json.loads(response.data) == {'message': 'Success'}

    def test_response_entity_initialization(self):
        entity = ResponseEntity()
        assert entity.data is (None,)
        assert entity.status is (None,)
        assert entity.mimetype == 'application/json'


if __name__ == '__main__':
    unittest.main()
