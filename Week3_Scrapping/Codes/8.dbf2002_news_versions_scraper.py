import re
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class DBFVersionScraper:
    """Scrape DBF Viewer 2000 version history from dbf2002.com/news.html"""

    def __init__(self, url="https://www.dbf2002.com/news.html", headless=True):
        """Initialize scraper with URL, headless mode, and output file path."""
        self.url = url
        self.headless = headless
        self.driver = None
        self.output_file = "./scraped_versions/dbf_versions.csv"

    def setup_driver(self):
        """Set up Chrome WebDriver with headless option."""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        service = Service()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def scrape_versions(self):
        """Scrape version numbers, release dates, and save them to a CSV file."""
        self.driver.get(self.url)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        today = datetime.now().strftime("%d-%m-%Y")

        # Regex pattern for versions and dates
        pattern = r"(v[\d\.]+),(\d{2}-\d{2}-\d{4})"
        matches = re.findall(pattern, body_text)

        data = []
        for version, date in matches:
            data.append({
                "Version": version,
                "Date": date,
                "URL": self.url  # main page URL
            })

        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        df.to_csv(self.output_file, index=False, encoding="utf-8-sig")
        print(f"Saved {len(df)} versions to {self.output_file}")

    def close_driver(self):
        """Close the Chrome WebDriver."""
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    """Run the DBF Viewer 2000 version scraper."""
    scraper = DBFVersionScraper()
    scraper.setup_driver()
    scraper.scrape_versions()
    scraper.close_driver()
