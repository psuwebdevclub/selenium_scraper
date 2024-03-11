# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

# Define the Problem class
class Problem():
    def __init__(self, title, success, link, problem_type):
        self.title = title
        self.success = success
        self.problem_link = link    
        self.problem_type = problem_type

# Define the URL of the website to scrape
url = "https://leetcode.com/problemset/?difficulty=HARD&page=1&listId=wpwgkgt" #We could always change this to the next page

# Initialize the Chrome webdriver
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Uncomment this line to run the browser in headless mode

driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get(url)

time.sleep(5) # Wait for the page to load

elements = []

# Find all divs with role="row" within the rowgroup div
rows = driver.find_elements(By.CSS_SELECTOR, 'div[role="row"]')

# Iterate over each row and find divs with role="cell"
for row in rows:
    cells = row.find_elements(By.CSS_SELECTOR, 'div[role="cell"]')
    title = None
    success = None
    link = None
    problem_type = None

    for cell in cells:
        text = cell.text.strip() # Remove leading and trailing spaces from text
        if "%" in text: 
            success = text
        elif "Easy" in text.split(' ') or "Medium" in text.split(' ') or "Hard" in text.split(' '):
            problem_type = text
        elif "." in text:
            title = text
        a_tags = cell.find_elements(By.TAG_NAME, 'a')
        for a_tag in a_tags:
            if len(a_tag.get_attribute('href')) > 10 and "subscribe" not in a_tag.get_attribute('href'):
                link = a_tag.get_attribute('href')

    if title and success and link and problem_type:
        elements.append(Problem(title, success, link, problem_type))

# Print the scraped data
for element in elements:
    print(element.title)
    print(element.success)
    print(element.problem_link)
    print(element.problem_type)
    print("\n")