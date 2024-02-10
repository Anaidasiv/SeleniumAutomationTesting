import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def testHomeSubmission(self, getData):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["fname"])
        homePage.getEmail().send_keys(getData["lname"])
        homePage.checkBox().click()
        # Static Dropdown
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitForm().click()
        message = homePage.getSuccessMsg().text
        print(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
