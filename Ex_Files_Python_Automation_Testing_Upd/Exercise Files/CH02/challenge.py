from selenium import webdriver
from selenium.webdriver.common.by import By

# open driver
driver = webdriver.Chrome()
# going to URL
driver.get("https://www.python.org/")
# find by id
element_by_id = driver.find_element(By.ID, "submit")
print(element_by_id)
# find by name
element_by_name = driver.find_element(By.NAME, "submit")
print(element_by_name)
# find by xpath
element_by_xpath = driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/h1/a/img')
print(element_by_xpath)
# find by class
element_by_class = driver.find_element(By.CLASS_NAME, "search-button")
print(element_by_class)
# close the driver
driver.close()