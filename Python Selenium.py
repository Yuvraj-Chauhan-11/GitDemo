import time

from selenium import webdriver
# there is a middle man involve called Chrome driver service to invoke the chrome driver , when we invoke the
# chrome driver they relase a verison and with that it goes to internet and download the chrome and opemn it to you/

driver = webdriver.Chrome()

driver.get("https://www.rahulshettyacademy.com")
driver.maximize_window()
print(driver.title) # grab the title of the page
print(driver.current_url)







time.sleep(2)