```python
import os
from typing import List, Dict
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class VectorDatabase:
    def __init__(self):
        self.client = MongoClient(os.getenv('DB_URI'))
        self.db = self.client[os.getenv('DB_NAME')]
        self.collection = self.db[os.getenv('DB_COLLECTION')]

    def insert_data(self, data: List[Dict]):
        self.collection.insert_many(data)

    def query_data(self, query: Dict):
        return self.collection.find(query)

    def update_data(self, query: Dict, new_data: Dict):
        self.collection.update_many(query, {"$set": new_data})

    def delete_data(self, query: Dict):
        self.collection.delete_many(query)
```