#from vebelement_alert import *
from webelement_class import *

driver=webdriver.Chrome(executable_path='../../drivers/chromedriver 2')
driver.implicitly_wait(10)
driver.maximize_window()

email="my_cool_email@gmail.com"

#test_alert_one_button()
#test_alert_two_button()
#test_go_to_authentication_page(driver)
#test_create_account(driver, email)
#click_element_by_locator(driver, '//*[@id="authentication"]')
#test_explicit_wait(driver)
test_drag_and_drop(driver)
#test_mouse_hover_over(driver)

sleep(5)
driver.quit()
