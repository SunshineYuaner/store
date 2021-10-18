'''
    HTMLTestRunner
    联网安装
'''
from HTMLTestRunner import HTMLTestRunner
import unittest
# 加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\day08\day13【单元测试】\代码\day13",pattern="*Test.py")


# 创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "计算器的测试报告",
    description="这是计算器加法测试报告",
    verbosity=1,
    stream = open(file="计算器测试报告.html",mode="w+",encoding="utf-8")
)

# 执行用例
runner.run(tests)


#  任务1：实现代码发送一封邮件，并把测试报告当成附件。@qq.com
'''
    密码：不是邮箱登陆密码，邮箱的授权码，先开启邮箱的smtp的授权码。
'''









