# Week3/Web_Scrapping

## Selenium WebDriver for Web Scraping — Full Documentation

---

### 1.What Is Selenium?

**Selenium** is a powerful **web automation framework** that lets you control browsers using code.

Originally built for **automated testing**, it’s also used for **web scraping dynamic websites** — i.e., pages that load content with JavaScript (which simple tools like `requests` or `BeautifulSoup` can’t easily handle).

---

### 2.Why Use Selenium for Scraping?

- Handles **JavaScript-rendered content**
- Simulates **real user actions** (clicks, scrolls, typing)
- Works with **any browser** — Chrome, Firefox, Edge, etc.
- Supports **headless mode** (runs without opening a visible browser window)

---

### 3.Installation Steps

**Step 1: Install Python**

If you don’t already have it:

```bash
python --version

```

If not installed, download from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Make sure to **check “Add to PATH”** during installation.

---

**Step 2: Install Selenium**

Open Command Prompt or Terminal and run:

```bash
pip install selenium

```

---

**Step 3: Install WebDriver Manager**

This automatically handles the correct ChromeDriver/GeckoDriver versions for your browser:

```bash
pip install webdriver-manager

```

---

### 4.Basic Concept: How Selenium Works

Think of Selenium like this:

1. You **create a browser instance** (like opening Chrome).
2. You **load a webpage** (like typing a URL).
3. You **locate elements** on the page using tags, class names, etc.
4. You **extract data** or **interact** (click, type, etc.).
5. You **close** the browser when done.

---

### 5.Setting Up the WebDriver

Example: Setting up Chrome in Python

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
options = Options()
options.add_argument("--headless=new")  # run in background
options.add_argument("--window-size=1920,1080")

# Start Chrome WebDriver automatically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

```

   **Explanation:**

- `Options()` → lets you set Chrome behavior (headless, window size, etc.)
- `ChromeDriverManager().install()` → downloads the right ChromeDriver automatically
- `webdriver.Chrome()` → opens a Chrome browser controlled by Python

---

### 6.Opening a Web Page

```python
driver.get("https://en.wikipedia.org/wiki/Java_version_history")
print(driver.title)

```

Loads the webpage and prints the title.

---

**Finding Elements on the Page**

Selenium provides many **locator methods** inside the `By` class:

| Method | Example | Description |  |
| --- | --- | --- | --- |
| `By.ID` | `driver.find_element(By.ID, "username")` | Finds element by its HTML `id` |  |
| `By.NAME` | `driver.find_element(By.NAME, "q")` | Finds element by its `name` attribute |  |
| `By.CLASS_NAME` | `driver.find_elements(By.CLASS_NAME, "price")` | Finds all with same class |  |
| `By.TAG_NAME` | `driver.find_elements(By.TAG_NAME, "table")` | Finds all tables |  |
| `By.LINK_TEXT` | `driver.find_element(By.LINK_TEXT, "Next")` | Finds link by visible text |  |
| `By.CSS_SELECTOR` | `driver.find_element(By.CSS_SELECTOR, "div.container > h2")` | CSS selector style |  |
| `By.XPATH` | `driver.find_element(By.XPATH, "//div[@class='title']")` | Finds by XPath expression |  |

---

### 8.Extracting Data (Text or Attributes)

```python
heading = driver.find_element(By.TAG_NAME, "h1").text
print("Heading:", heading)

links = driver.find_elements(By.TAG_NAME, "a")
for link in links[:5]:
    print(link.text, "-", link.get_attribute("href"))

```

`.text` → returns visible text

`.get_attribute("href")` → gets attribute value (e.g., link URL)

---

### 9.Scraping HTML Tables Example (Wikipedia)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Setup Chrome
options = Options()
options.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open page
url = "https://en.wikipedia.org/wiki/Java_version_history"
driver.get(url)

# Find all tables
tables = driver.find_elements(By.TAG_NAME, "table")
dataframes = []

# Convert each table to pandas DataFrame
for table in tables:
    html = table.get_attribute('outerHTML')
    df = pd.read_html(html)[0]
    dataframes.append(df)

# Combine into one CSV
final_df = pd.concat(dataframes, ignore_index=True)
final_df.to_csv("java_version_history.csv", index=False)

print("Data saved to java_version_history.csv")

driver.quit()

Handling Dynamic Content (JavaScript-loaded data)
```

---

### 10.Handling Dynamic Content (JavaScript-loaded data)

Some websites load content **after** the page loads.

Use **explicit waits** to wait for elements before scraping:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait until a specific element appears
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "version-table"))
)
print("Table found!")

```

---

### 11.Useful Selenium Actions for Scraping

| Action | Example | Description |
| --- | --- | --- |
| Scroll down | `driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")` | Load more data |
| Click element | `element.click()` | Simulate click |
| Enter text | `element.send_keys("Python", Keys.RETURN)` | Type into input |
| Go back | `driver.back()` | Navigate backward |
| Refresh page | `driver.refresh()` | Reload page |

---

### 12.Common Errors and Fixes

| Error | Cause | Fix |
| --- | --- | --- |
| `selenium.common.exceptions.WebDriverException` | Missing driver | Install using webdriver-manager |
| `NoSuchElementException` | Wrong locator | Use correct `By.XPATH` or `By.CSS_SELECTOR` |
| Browser doesn’t open | Mismatched Chrome/driver version | webdriver-manager handles this automatically |
| Page loads slowly | Element not ready | Use `WebDriverWait` |

---

### 13.Closing or Quitting Driver

Always close the browser after scraping:

```python
driver.quit()

```

---

### 14.Headless vs Normal Mode

- **Headless Mode** → runs invisibly (faster, used for automation)
- **Normal Mode** → opens browser window (useful for debugging)

Set in Chrome options:

```python
options.add_argument("--headless=new")  # or comment this line to see the browser

```

---

### 15.Exporting Data

After extracting data into a Python list or DataFrame, you can export:

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)

```

---

### 16.Best Practices for Web Scraping with Selenium

- Use **headless mode** for speed.
- Always use **explicit waits** instead of `time.sleep()`.
- Respect **robots.txt** and website policies.
- Avoid sending too many requests too quickly.
- Store intermediate results in **CSV or JSON**.
- Use **try–except** blocks to handle missing elements gracefully.

---

### 17.Example: Full Working Web Scraper

```python
"""
Script Name: selenium_web_scraper.py
Description:
    Demonstrates using Selenium WebDriver with Python
    to scrape dynamic web data (Wikipedia Java version history)
    and store it in a CSV file.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup Chrome
options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the target page
url = "https://en.wikipedia.org/wiki/Java_version_history"
driver.get(url)

# Wait for content to load
time.sleep(3)

# Extract tables
tables = driver.find_elements(By.TAG_NAME, "table")
df_list = [pd.read_html(table.get_attribute("outerHTML"))[0] for table in tables]

# Combine and save
final_df = pd.concat(df_list, ignore_index=True)
final_df.to_csv("java_version_history.csv", index=False)

print("Data scraped and saved successfully!")

driver.quit()

```