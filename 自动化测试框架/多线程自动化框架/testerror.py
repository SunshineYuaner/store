from selenium import webdriver
from unittest import TestCase
from case import case
from main import main
from ddt import ddt
from ddt import data

@ddt
class test2(TestCase):
    @data(*case.login_error_data)
    def testcasserror(self, testdata):
        username = testdata["username"],
        passwork = testdata["passwork"]
        expect = testdata["expect"]

        driver = webdriver.Chrome()
        loginop = main(driver)
        loginop.login(username, passwork)

        result = loginop.getError_result()
        driver.quit()

        self.assertEqual(expect, result)