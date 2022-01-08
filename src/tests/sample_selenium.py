from selenium import webdriver
from time import *
driver=webdriver.Chrome(executable_path='../../drivers/chromedriver 2')
driver.get("https://www.thelevelupsolutions.com/")
driver.implicitly_wait(5)
driver.maximize_window()
sleep(2)
driver.quit()