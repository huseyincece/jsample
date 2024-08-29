from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the application
driver.get("http://localhost:5000")

# Wait for the page to load
time.sleep(3)

# Check the title
assert "Hello, CI/CD Pipeline with Jenkins!" in driver.page_source

# Close the browser
driver.quit()
