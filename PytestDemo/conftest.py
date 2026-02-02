import pytest
from selenium import webdriver


@pytest.fixture(scope="class") # pre condition
def setup():
    print("I ll be executing first")
    yield # after condition
    print("I ll be executing last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome","Yuvraj","Chauhan"),("FireFox","NTT Data"),("IE","SS")])
def crossBrowser(request):
    return request.param

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.firefox()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
