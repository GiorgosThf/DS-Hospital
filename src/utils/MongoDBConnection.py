from pymongo import MongoClient

from src.utils.EnvironmentConfig import Config


class MongoDBConnection:
    def __init__(self, host=None, port=None, db_name=None ):
        self.host = host or Config.HOST.value
        self.port = port or Config.PORT.value
        self.db_name = db_name or Config.DB.value
        self.client = None
        self.db = None

    def connect(self):
        if not self.client:
            self.client = MongoClient(
                host=self.host,
                port=self.port,
            )
            self.db = self.client[self.db_name]
        return self.db

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None
