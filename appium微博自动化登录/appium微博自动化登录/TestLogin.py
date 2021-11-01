from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from InitPage import InitPage
from LoginOperation import LoginOperation
from appium import webdriver


@ddt
class TestLogin(TestCase):

    @data(*InitPage.login_success_date)
    def testLoginSuccess(self, testdata):
        username = testdata["username"]
        pwd = testdata["pwd"]
        expect = testdata["expect"]

        # 执行登陆
        data = {
            "deviceName": "vivo X27 Pro",
            "platformName": "Android",
            "platformVersion": "10",
            "appPackage": "com.sina.weibo",
            "appActivity": ".SplashActivity",
            "skipServerInstallation": True,
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", data)
        driver.implicitly_wait(8)
        loginop = LoginOperation(driver)

        loginop.login(username, pwd)

        #  获取实际结果
        result = loginop.getSuccess_result()
        if result != expect:
            driver.save_screenshot("img/222.png")
        driver.quit()
        self.assertEqual(result, expect)

    @data(*InitPage.login_error_data)
    def testLoginError(self, testdata):
        username = testdata["username"]
        pwd = testdata["pwd"]
        expect = testdata["expect"]

        # 执行登陆
        data = {
                    "deviceName": "vivo X27 Pro",
                    "platformName": "Android",
                    "platformVersion": "10",
                    "appPackage": "com.sina.weibo",
                    "appActivity": ".SplashActivity",
                    "skipServerInstallation": True,
                }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", data)
        loginop = LoginOperation(driver)

        loginop.login(username, pwd)

        #  获取实际结果
        result = loginop.getError_result()
        if result != expect:
            driver.save_screenshot("img/111.png")
        driver.quit()
        self.assertEqual(result, expect)
