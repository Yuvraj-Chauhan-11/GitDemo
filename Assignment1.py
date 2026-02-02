import timemanagemnet

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

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
accesstext = driver.find_element(By.CSS_SELECTOR, "#interview-material-container div:nth-child(2) p:nth-child(2)").text
print(accesstext)
var = accesstext.split("Please email us at ")

finaltext = var[1].split(" with below template to receive response")


final =finaltext[0]
print(final)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(final)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys(final)
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#login-form div")))
print(driver.find_element(By.CSS_SELECTOR,"#login-form div").text)

