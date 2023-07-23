```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_scraper import config

class DynamicContentHandler:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def handle_dynamic_content(self, url):
        self.driver.get(url)

        while True:
            try:
                self.wait.until(EC.presence_of_element_located((By.ID, config.DYNAMIC_CONTENT_ID)))
                time.sleep(config.DYNAMIC_CONTENT_DELAY)
            except Exception as e:
                print(f"Error while waiting for dynamic content: {e}")
                break

        page_source = self.driver.page_source
        self.driver.quit()

        return page_source
```