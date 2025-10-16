from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import os

class WindowsServerScraper:
    """Scrapes Windows Server release information from Microsoft's official site."""

    def __init__(self, url="https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info", headless=True):
        self.url = url
        self.headless = headless
        self.driver = None
        self.xpath_table = '//table[contains(@class,"table")]'
        self.output_file = "./scraped_versions/windows_server.csv"

    def setup_driver(self):
        """Configure and initialize the Chrome WebDriver."""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        service = Service()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def scrape_table(self):
        """Scrape the Windows Server release table and save it as a CSV file."""
        print(f"🔹 Scraping: {self.url}")
        self.driver.get(self.url)
        today = datetime.now().strftime("%d-%m-%Y")

        table = self.wait.until(EC.presence_of_element_located((By.XPATH, self.xpath_table)))
        rows = table.find_elements(By.TAG_NAME, "tr")
        data = []

        headers = [th.text.strip() for th in rows[0].find_elements(By.TAG_NAME, "th")]
        for row in rows[1:]:
            cells = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
            if not cells: continue
            row_dict = {headers[i] if i < len(headers) else f"Column{i+1}": cells[i] for i in range(len(cells))}
            row_dict["Scraped Date"] = today
            data.append(row_dict)

        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        df.to_csv(self.output_file, index=False, encoding='utf-8-sig')
        print(f"Saved {len(df)} rows to {self.output_file}")

    def close_driver(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    scraper = WindowsServerScraper()
    scraper.setup_driver()
    scraper.scrape_table()
    scraper.close_driver()
