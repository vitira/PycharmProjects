from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#1. Open the browser
driver=webdriver.Chrome(executable_path='../../drivers/chromedriver 2')
driver.implicitly_wait(5)
driver.maximize_window()

#2 Open google page
driver.get("https://www.google.com/")

#3 Search for selenium
search_box=driver.find_element(By.NAME, 'q')
search_box.send_keys("Selenium")
search_box.send_keys(Keys.ENTER)

#4 Capture result text
text_result=driver.find_element(By.XPATH, '//*[@id="result-stats"]').text
print(text_result)
