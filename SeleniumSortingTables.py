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
browsersortedveggies = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggieWebElements:
    browsersortedveggies.append(ele.text)
print(browsersortedveggies)
originalbroswerSortedlist = browsersortedveggies.copy()
print(originalbroswerSortedlist)

assert browsersortedveggies == originalbroswerSortedlist