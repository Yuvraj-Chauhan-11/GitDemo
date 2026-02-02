import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
# Implicit Wait
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click() # partial text syntax for xpath
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
time.sleep(2)

for product in products:
    productname = product.find_element(By.XPATH, "div/h4/a").text
    if productname == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
        time.sleep(1)


driver.find_element(By.XPATH, "//a[contains(@class, 'btn-primary')]").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class = 'checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//form/input[@value='Purchase']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
print(successText)
assert successText in ("Thank you")
time.sleep(4)

