```python
# web_scraper/config.py

# List of keywords to be scraped
KEYWORDS = ["keyword1", "keyword2", "keyword3"]

# DOM element IDs
DOM_ELEMENT_IDS = {
    "pagination": "pagination-id",
    "dynamic_content": "dynamic-content-id",
    "data": "data-id"
}

# Message names
MESSAGE_NAMES = {
    "data_extraction_complete": "DATA_EXTRACTION_COMPLETE",
    "error": "ERROR"
}

# Function names
FUNCTION_NAMES = {
    "initiate_scraping": "initiate_scraping",
    "handle_pagination": "handle_pagination",
    "handle_dynamic_content": "handle_dynamic_content",
    "extract_data": "extract_data"
}

# Database connection details
DATABASE_CONNECTION = {
    "host": "localhost",
    "port": 5432,
    "database": "vector_database",
    "user": "user",
    "password": "password"
}
```