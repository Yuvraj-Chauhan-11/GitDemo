import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        checkbox.is_selected()
        break


radiobutton = driver.find_elements(By.XPATH,"//input[@name='radioButton']")

for radio in radiobutton:
    if radio.get_attribute("value") == "radio3":
        radio.click()
        assert radio.is_selected()
        break
time.sleep(3)

# if we want to know whether element is displayed on the web page or not , is displayed method is helpful





