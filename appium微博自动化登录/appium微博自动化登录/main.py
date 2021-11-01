from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title = "微博app测试报告",
    description= "微博app登陆测试",
    verbosity=1,
    stream = open(file="微博app登录测试.html",mode="w+",encoding="utf-8")
)

runner.run(tests)

# 邮件发送模块





