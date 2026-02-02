import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# Implicit Wait
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")



Action = ActionChains(driver)
Action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
Action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
time.sleep(2)
Action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(2)

