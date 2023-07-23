```python
import requests
from bs4 import BeautifulSoup
from config import BASE_URL, PAGE_PARAM, DOM_PAGINATION_ID

def get_page_content(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def get_next_page_url(soup):
    pagination_element = soup.find(id=DOM_PAGINATION_ID)
    if pagination_element:
        next_page = pagination_element.find('a', {'rel': 'next'})
        if next_page and 'href' in next_page.attrs:
            return BASE_URL + next_page['href']
    return None

def handle_pagination(url):
    while url:
        soup = get_page_content(url)
        yield soup
        url = get_next_page_url(soup)
```