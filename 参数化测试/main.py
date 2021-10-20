from HTMLTestRunner import HTMLTestRunner
import unittest
import os
# 加载所有用例
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")


# 创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "银行的测试报告",
    description="这是银行开户，存钱，取钱，转账测试报告",
    verbosity=1,
    stream = open(file="银行测试报告.html",mode="w+",encoding="utf-8")
)

# 执行用例
runner.run(tests)