import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    @pytest.mark.usefixtures("setup")
    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # cards = self.driver.find_elements_by_css_selector(".card-title a")
        log.info("getting card details")
        cards = checkoutPage.getCardTitle()
        # cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        i = -1

        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()
        # self.driver.switch_to.window(self.driver.current_window_handle)

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmPage = checkoutPage.checkOutItems()
        log.info("enter country details")
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info("text received matches"+textMatch)
        assert ("Success! Thank you!" in textMatch)
