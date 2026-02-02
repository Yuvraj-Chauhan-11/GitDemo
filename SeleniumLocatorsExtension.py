import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input[type='password']").send_keys("Hello@1234")
driver.find_element(By.ID,"confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

time.sleep(3)