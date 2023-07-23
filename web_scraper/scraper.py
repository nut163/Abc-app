```python
import requests
from bs4 import BeautifulSoup
from .config import KEYWORDS
from .pagination_handler import handle_pagination
from .dynamic_content_handler import handle_dynamic_content
from .data_extractor import extract_data
from .database.vector_database import VectorDatabase

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.database = VectorDatabase()

    def start_scraping(self):
        page_content = self._get_page_content(self.base_url)
        dynamic_content = handle_dynamic_content(page_content)
        self._scrape_page(dynamic_content)

    def _get_page_content(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')

    def _scrape_page(self, page_content):
        for keyword in KEYWORDS:
            data = extract_data(page_content, keyword)
            self.database.store_data(data)

        next_page_url = handle_pagination(page_content)
        if next_page_url:
            next_page_content = self._get_page_content(next_page_url)
            self._scrape_page(next_page_content)
```
