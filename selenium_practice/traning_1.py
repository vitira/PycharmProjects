from selenium import webdriver
# 1. open the browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()


# 2. open the google.com
driver.get("http://google.com")

# 3. search for 'selenium'
search_window=driver.find_element_by_name("q")


# entering the text in the input (text) form
search_window.send_keys("Selenium")
search_window.send_keys(Keys.ENTER)
# 4. capture the result text
result_message = driver.find_element(By.ID, "result-stats").text
print("I got result here: ", result_message)

# 5. close the browser
# driver.close()   # closes current tab
# close all tabs