from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# copied the chromedriver to /usr/local/bin
driver = webdriver.Chrome()
# or specify the path: driver = webdriver.Chrome('/Users/vitaliididkivskyi/Downloads/chromedriver')


driver.get("https://google.com")

search_text_box = driver.find_element_by_name("q")
search_text_box.clear()
search_text_box.send_keys("python selenium integration")
search_text_box.send_keys(Keys.RETURN)

driver.close()