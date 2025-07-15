import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
'''
1. Go to https://wiki.python.org/moin/FrontPage
2. Perform a search for the text "Beginner"
3. In the left-side menu bar, change the value of the select from "More Options" to "Raw Text"
'''

driver = webdriver.Chrome()
driver.get('https://wiki.python.org/moin/FrontPage')


input_id = driver.find_element(By.ID, 'searchinput')
dropidXpath = '//*[@id="sidebar"]/div[3]/ul/li[5]/form/div/select'
send_text = 'Beginner'

input_id.clear()
input_id.send_keys(send_text)
#input_id.submit()
# other solution
input_id.send_keys(Keys.RETURN)
time.sleep(5)

drop_down = driver.find_element(By.XPATH, dropidXpath)
# drop_down = driver.find_element(By.NAME, 'action')
select = Select(drop_down)
# select.select_by_index(2)
select.select_by_visible_text('Raw Text')
time.sleep(2)
driver.close()
