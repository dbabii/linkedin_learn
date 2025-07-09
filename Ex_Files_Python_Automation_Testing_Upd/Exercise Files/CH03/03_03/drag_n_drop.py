import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://jqueryui.com/droppable')
# select a frame
driver.switch_to.frame(0)
# create an object of Action Chains Class
action_chains = ActionChains(driver)
# define source and target positions
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

# move the source by offset
action_chains.drag_and_drop_by_offset(source, 100, 150).perform()
time.sleep(2)
# move the element to target
action_chains.drag_and_drop(source, target).perform()
time.sleep(2)
driver.close()