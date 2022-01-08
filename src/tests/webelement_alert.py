'''Sweetch to allert practice here:
https://courses.letskodeit.com/practice'''
from selenium import webdriver
#veriable
from selenium.webdriver.common.by import By

HOST=("https://courses.letskodeit.com/practice")
name="John Dough"
#open the browser
driver=webdriver.Chrome(executable_path='../../drivers/chromedriver 2')

driver.implicitly_wait(10)
driver.maximize_window()

#open automation practice site
driver.get(HOST)
def test_alert_one_button():
#enter name
    name_input=driver.find_element(By.XPATH, '//*[@id="name"]')
    name_input.send_keys(name)
#click on alert
    driver.find_element(By.XPATH, '//*[@id="alertbtn"]').click()

#switch to alert
    alert=driver.switch_to.alert
#get the text
    print("Switch to alert text:", alert.text)
#click ok on alert
    alert.accept()
    print("###################################")
def test_alert_two_button():
#enter name
    input_name2=driver.find_element(By.XPATH, '//*[@id="name"]')
    input_name2.send_keys(name)
#click on confirm
    driver.find_element(By.XPATH, '//*[@id="confirmbtn"]').click()
#switch to alert
    alert2=driver.switch_to.alert
#get the text
    print("Switch to alert text: ", alert2.text)
#click cancel
    alert2.dismiss()



