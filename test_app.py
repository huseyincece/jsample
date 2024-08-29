from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:5000")
assert "Hello, World!" in driver.page_source
driver.quit()
