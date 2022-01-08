from time import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#veriables
email="mycool@email.com"
cust_fname="John"
cust_lname="Doe"
password="forget_me_as_usual123"
state="New Jersey"
filepath="../screenshots/"

#steps
#1. Open the browserƒ
driver=webdriver.Chrome(executable_path='../../drivers/chromedriver 2')
driver.implicitly_wait(20) #synchronizing the browser
driver.maximize_window()

# open the automationpractice.com demo website
url="https://jqueryui.com/droppable/"
driver.get(url)
driver.switch_to.frame(0)

from_frame=driver.find_element(By.ID, "draggable")
to_frame=driver.find_element(By.ID, "droppable")
sleep(2)
actions=ActionChains(driver)
actions.drag_and_drop(from_frame, to_frame).perform()
actions.click_and_hold(from_frame).move_to_element(to_frame).perform()





