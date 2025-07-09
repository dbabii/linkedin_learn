from selenium import webdriver
from selenium.webdriver.common.by import By

# assignee to driver a Chrome browser
driver = webdriver.Chrome()
# open URL
driver.get("file:///home/grom/git/linkedin_learn/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html")
# find a login form on the page
login_form = driver.find_element(By.ID, "loginForm")
# print the information into console
print("My login form element is:", login_form)
driver.close()