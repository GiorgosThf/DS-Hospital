import unittest
from unittest.mock import patch, MagicMock

from src.utils.EnvironmentConfig import Config
from src.utils.MongoDBConnection import MongoDBConnection


class TestMongoDBConnection(unittest.TestCase):

    @patch('src.utils.MongoDBConnection.MongoClient')
    def test_connect(self, mock_mongo_client):
        # Setup mock client
        mock_client_instance = MagicMock()
        mock_mongo_client.return_value = mock_client_instance

        # Initialize MongoDBConnection
        connection = MongoDBConnection(host='localhost', port=27017, db_name='testdb')

        # Connect to the database
        db = connection.connect()

        # Assertions
        mock_mongo_client.assert_called_once_with(host='localhost', port=27017)
        self.assertEqual(db, mock_client_instance['testdb'])
        self.assertIsNotNone(connection.client)
        self.assertIsNotNone(connection.db)

    @patch('src.utils.MongoDBConnection.MongoClient')
    def test_connect_with_defaults(self, mock_mongo_client):
        # Setup mock client
        mock_client_instance = MagicMock()
        mock_mongo_client.return_value = mock_client_instance

        # Initialize MongoDBConnection without parameters
        connection = MongoDBConnection()

        # Connect to the database
        db = connection.connect()

        # Assertions
        mock_mongo_client.assert_called_once_with(host='mongodb', port=27017)
        self.assertEqual(db, mock_client_instance['DigitalHospital'])
        self.assertIsNotNone(connection.client)
        self.assertIsNotNone(connection.db)

    @patch('src.utils.MongoDBConnection.MongoClient')
    def test_close(self, mock_mongo_client):
        # Setup mock client
        mock_client_instance = MagicMock()
        mock_mongo_client.return_value = mock_client_instance

        # Initialize MongoDBConnection
        connection = MongoDBConnection(host='localhost', port=27017, db_name='testdb')

        # Connect to the database
        connection.connect()

        # Close the connection
        connection.close()

        # Assertions
        mock_client_instance.close.assert_called_once()
        self.assertIsNone(connection.client)
        self.assertIsNone(connection.db)


if __name__ == '__main__':
    unittest.main()
