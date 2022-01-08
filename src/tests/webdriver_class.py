# The WebDriver class provides a number of properties or attributes for browser
# interaction. We can use the properties and methods of the WebDriver class to interact
# with the browser window, alerts, frames and pop-up windows. It also provides
# features to automate browser navigation, access cookies, capture screenshots, and
# so on. In this chapter, we will explore some of the most important features of the
# WebDriver class.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Open the browser
driver=webdriver.Chrome(executable_path='../../drivers/chromedriver 2')
driver.implicitly_wait(5)


filepath= '../../screenshots/'


# 2. Open the automation practice demo website
driver.get("http://automationpractice.com/index.php")
search_box=driver.find_element(By.XPATH, '//*[@id="search_query_top"]')
search_box.send_keys('dress'+Keys.ENTER)

# Try following WebDriver property/attributes or methods:
# current url, current window handle, name, title, window_handles
# back(), forward(), refresh(), switch_to.window(window_name)

url=driver.current_url
browser_name=driver.current_window_handle
name=driver.name
title=driver.title
win_names=driver.window_handles

print("This is url:", url)
print("This is browser:", browser_name)
print("This is name:", name)
print("This is title:", title)
print("This is windows names:", win_names)
driver.save_screenshot(filepath+"screenshot1.png")

print('###################webdriver method##########################')
#back(), forward(), refresh(), switch_to.window(window_name)
driver.back()
time.sleep(2)
print("Curent URL:", url)
driver.save_screenshot(filepath+"screenshot_back.png")

driver.forward()
time.sleep(2)
print("Curent URL:", url)
driver.save_screenshot(filepath+"screenshot_forward.png")

driver.refresh()
time.sleep(2)
print("Curent URL:", url)
driver.save_screenshot(filepath+"screenshot_refresh.png")

print(" ################# switch_to.window(window_name) ##########")
products = driver.find_elements(By.XPATH, "//div[@id='center_column']//a[@class='product-name']")
products[0].click()
time.sleep(5)
time.sleep(5)
driver.save_screenshot(filepath+"last_dress_in_list.png")
#find element fb_btn
print("###########fb_button##########")
fb_btn=driver.find_element(By.XPATH, '//*[@id="center_column"]/div/div/div[3]/p[7]/button[2]').click()

#switch to window
win_names = driver.window_handles
print(win_names)
print(driver.title)
time.sleep(2)
driver.switch_to.window(win_names[-1])
driver.save_screenshot(filepath+'fb_screenshot.png')
#enter email
e_mail=driver.find_element(By.XPATH, '//*[@id="email"]')
e_mail.send_keys("myemail12345@gmail.com")
#enter password
my_password=driver.find_element(By.XPATH, '//*[@id="pass"]')
my_password.send_keys('i_do_not_know_this_psw')
time.sleep(2)
#take screenshot
driver.save_screenshot(filepath+'window_handle_work.png')





driver.quit()
