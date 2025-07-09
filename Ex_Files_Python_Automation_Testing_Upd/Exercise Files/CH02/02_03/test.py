from selenium import webdriver
from selenium.webdriver.common.by import By

# assignee to driver a Chrome browser
driver = webdriver.Chrome()
# open URL
driver.get("file:///home/grom/git/linkedin_learn/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html")
# find a login form on the page by ID
login_form = driver.find_element(By.ID, "loginForm")
# find an username on the page by name
username = driver.find_element(By.NAME, "username")
# find a login form by XPath with absolute path
login_form_xpath_abs = driver.find_element(By.XPATH, "/html/body/form[1]")
# find a login form by XPath with relative path
login_form_xpath_rel = driver.find_element(By.XPATH, "//form[1]")
# find a login form by XPath with relative path and using id
login_form_xpath_id = driver.find_element(By.XPATH, "//form[@id='loginForm']")
# find a class
content = driver.find_element(By.CLASS_NAME, "content")

# print the information into console
print("My login form element is:", login_form)
# print the output from the user
print("Username:", username)
# print login forms found in different ways
print("Login forms:")
print(login_form_xpath_abs)
print(login_form_xpath_rel)
print(login_form_xpath_id)
print("Content:", content)
driver.close()