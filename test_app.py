from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:5000")
assert "Hello, Jenkins CI/CD!" in driver.page_source
driver.quit()