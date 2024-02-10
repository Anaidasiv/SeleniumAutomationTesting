from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    success = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def checkBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.success)
