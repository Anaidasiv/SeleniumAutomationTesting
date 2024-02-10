from selenium.webdriver.common.by import By


class ConfirmPage:
    confirmedItems = (By.XPATH, "//button[@class='btn btn-success']")
    pass

    def __init__(self,driver):
        self.driver = driver

    def confirmItems(self):
        return self.driver.find_element(*ConfirmPage.confirmedItems)

