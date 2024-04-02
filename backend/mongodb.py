# build a helper class and functions to connect to mongodb

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
load_dotenv()
import os

class MongodbHelper:
    
    def __init__(self):
        self.client = self._get_mongo_client(os.getenv('MONGO_URI'))
        self.db = self.client['test']
        self.collection = self.db['test']

    def _get_mongo_client(self, mongo_uri):
        """Establish connection to the MongoDB."""
        try:
            client = MongoClient(mongo_uri)
            print("Connection to MongoDB successful")
            return client
        except ConnectionFailure as e:
            print(f"Connection failed: {e}")
            return None
        
    def insert_one(self, data):
        """Insert a single document into the collection."""
        return self.collection.insert_one(data)
    
    def find_one(self, query):
        """Find a single document in the collection."""
        return self.collection.find_one(query)
    
    def delete_one(self, query):
        """Delete a single document in the collection."""
        return self.collection.delete_one(query)
    
    def drop_collection(self):
        """Drop the collection."""
        return self.collection.drop()
    
    def update_one(self, query, data):
        """Update a single document in the collection."""
        return self.collection.update_one(query, data)
    