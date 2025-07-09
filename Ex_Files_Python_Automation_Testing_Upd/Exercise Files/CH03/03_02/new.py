from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('file:///home/grom/git/linkedin_learn/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH03/03_02/html_code_03_02.html')

select = Select(driver.find_element(By.NAME, 'numReturnSelect'))
select.select_by_index(4)
time.sleep(2)
select.select_by_visible_text("250")
time.sleep(2)
select.select_by_value("500")
time.sleep(2)

options = select.options
print(options)

submit_button = driver.find_element(By.NAME, 'continue')
submit_button.submit()
time.sleep(2)
driver.close()