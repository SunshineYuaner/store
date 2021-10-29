# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/29 9:28
# 文件名：logintest.py
# 开发工具：PyCharm

from unittest import TestCase
from selenium import webdriver


class TestHkr(TestCase):

    def testLogin(self):
        # 1.准备数据
        username = "yuaner"
        pwd = "Hw000727."
        expect = "Student Login"

        # 2.执行用例
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        driver.find_element_by_xpath("//*[@id='submit']").click()

        # 3.获取实际结果
        result = driver.title
        driver.quit()
        self.assertEqual(result, expect)

    def testLoginError(self):
        # 1.准备数据
        username = "yuaner"
        pwd = "Hw0007271."
        expect = "账户名错误或密码错误!别瞎弄!"

        # 2.执行用例
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        driver.find_element_by_xpath("//*[@id='submit']").click()

        # 3.获取实际结果
        result = driver.find_element_by_xpath("//*[@id='msg_uname']").text
        driver.quit()
        self.assertEqual(result, expect)
