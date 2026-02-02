import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# Implicit Wait
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scroll(0,document.body.scrollHeight)") # Scroll to the bottom of the page
time.sleep(2)
driver.execute_script("window.scroll(0,600)") # SCROLL TO SOMEWHERE IN THE MIDDLE OF THE PAGE DEPENDS OF HEIGHT OF THE PAGE
time.sleep(2)
# Screenshot will be saved in png file using the below method
driver.get_screenshot_as_file("screen.png")

