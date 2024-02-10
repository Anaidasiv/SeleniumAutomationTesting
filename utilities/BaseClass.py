import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects import homePage
logging.basicConfig(filename="C:\\Users\\sreek\\PycharmProjects\\pythonselFramework\\tests\\logfile1.log", level=logging.INFO)


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getlogger(self):
        loggerName = self.__class__.__name__
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile1.log')  # name of the file is 'logfile.log'
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # fileHandler object it will take

        logger.setLevel(logging.INFO)
        logger.info("Information statement")
        return logger



