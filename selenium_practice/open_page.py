from selenium import webdriver
from selenium.webdriver.common import keys

# chromedriver executable is saved under /usr/local/bin/chromedriver
# - if there is an error: “chromedriver” cannot be opened because the developer cannot be verified
#   go to terminal and run the following command
#   xattr -d com.apple.quarantine /usr/local/bin/chromedriver
driver = webdriver.Chrome()

driver.get("http://www.google.com")
driver.implicitly_wait(10)
driver.find_element_by_name( "q" ).send_keys( "Selenium" + keys.Keys.RETURN)
##driver.quit()