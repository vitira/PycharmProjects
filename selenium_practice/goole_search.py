from selenium import webdriver
##from selenium.webdriver.common import keys

# chromedriver executable is saved under /usr/local/bin/chromedriver
# - if there is an error: “chromedriver” cannot be opened because the developer cannot be verified
#   go to terminal and run the following command
#   xattr -d com.apple.quarantine /usr/local/bin/chromedriver
## open browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
## open google com
driver.get("http://www.google.com")
## search for selenium
search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Selenium")
search_box.send_keys(Keys.ENTER)


## capture the result
## close the browser

#driver = webdriver.Chrome()

#driver.get("http://www.google.com")
#driver.implicitly_wait(10)
##driver.find_element_by_name( "q" ).send_keys( "Selenium" + keys.Keys.RETURN)
##driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# # 1. open the browser
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)  # synchronizing the browser
# driver.maximize_window()
#
# # 2. open the google.com
# driver.get("https://www.google.com/")
#
# # 3. search for 'selenium'
# search_box = driver.find_element(By.NAME, 'q')  # selenium 3, 4
# # entering the text in the input (text) form
# search_box.send_keys('selenium')
# search_box.send_keys(Keys.ENTER)
#
# # 4. capture the result text
# result_msg = driver.find_element(By.ID, 'result-stats').text
# print('I got the result here: \n\t', result_msg)
#
# # 5. close the browser
# # driver.close()   # closes current tab
# driver.quit()  # close all tabs