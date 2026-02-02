from selenium.webdriver.common.by import By

from PageObjects.Checkout_Confirmation import Checkout_Confirmation


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.shop_link = (By.XPATH, "//a[@href='/angularpractice/shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.XPATH, "//a[contains(@class, 'btn-primary')]")


    def add_product_to_cart(self,product_name):

        self.driver.find_element(*self.shop_link).click()  # partial text syntax for xpath
        products = self.driver.find_elements(*self.product_cards)


        for product in products:
            productname = product.find_element(By.XPATH, "div/h4/a").text
            if productname == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation