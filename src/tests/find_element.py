import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#1.Open the browser
driver=webdriver.Chrome(executable_path='../../drivers/chromedriver 2')
driver.implicitly_wait(5)
driver.maximize_window()

#2.Open automation practice demo website
driver.get("http://automationpractice.com/index.php")
search_box=driver.find_element(By.XPATH, "//input[@id='search_query_top']")
search_box.send_keys('dress' + Keys.ENTER)
time.sleep(2)
result=driver.find_element(By.CSS_SELECTOR, 'span.heading-counter').text
#result=driver.find_element(By.XPATH, '//*[@id="center_column"]/ul').text
print(result)
products=driver.find_elements(By.XPATH, "//div[@id='center_column']//a[@class='product-name']")
product_names=[]
for product in products:
    print(product.text)
    product_names.append(product.text.strip())
print(product_names)