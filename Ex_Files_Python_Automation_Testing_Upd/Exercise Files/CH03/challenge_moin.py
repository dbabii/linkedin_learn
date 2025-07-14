from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
'''
1. Go to https://wiki.python.org/moin/FrontPage
2. Perform a search for the text "Beginner"
3. In the left-side menu bar, change the value of the select from "More Options" to "Raw Text"
'''

driver = webdriver.Chrome()
driver.get('https://wiki.python.org/moin/FrontPage')

input_id = driver.find_element(By.ID, 'searchinput')
time.sleep(1)
input_id.clear()
input_id.send_keys('Beginner')
time.sleep(1)
input_id.submit()
time.sleep(1)

drop_down = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div[3]/ul/li[5]/form/div/select')
# drop_down = driver.find_element(By.NAME, 'action')
select = Select(drop_down)
# select.select_by_index(2)
select.select_by_visible_text('Raw Text')
time.sleep(2)
driver.close()
