```python
import requests
from bs4 import BeautifulSoup
from .config import KEYWORDS
from .database.vector_database import VectorDatabase

class DataExtractor:
    def __init__(self):
        self.db = VectorDatabase()

    def extract_data(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for keyword in KEYWORDS:
            data = soup.find_all(text=lambda text: text and keyword in text)
            if data:
                self.db.store_data(keyword, data)

    def handle_message(self, message):
        if message == 'EXTRACTION_COMPLETE':
            self.db.commit_data()
        elif message == 'EXTRACTION_ERROR':
            print("An error occurred during data extraction.")
```