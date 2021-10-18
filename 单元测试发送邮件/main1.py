from unittest import TestCase                   # 第二步
from HTMLTestRunner import HTMLTestRunner       # 第三步
import unittest                                 # 第三步

class Calc:                                     # 第一步
    def add(self,a,b):
        return  a + b

    def minus(self,a,b):
        return a - b

    def multi(self,a,b):
        return a * b

    def devision(self,a,b):
        return a / b

class CalcTest(TestCase):                       # 第二步
    # 加法
    def testAdd(self):
        a = -6
        b = 5
        c = -1

        calc = Calc()
        s = calc.add(a,b)

        # 判断用例是否通过
        self.assertEqual(s,c)
    # 减法
    def testMinus(self):
        a = 6
        b = 5
        c = 1

        calc = Calc()
        s = calc.minus(a,b)
        # 判断用例是否通过
        self.assertEqual(s,c)
    # 乘法
    def testMulti(self):
        a = 6
        b = 5
        c = 30

        calc = Calc()
        s = calc.multi(a,b)
        # 判断用例是否通过
        self.assertEqual(s,c)
    # 除法
    def testDevision(self):
        a = 30
        b = 5
        c = 6

        calc = Calc()
        s = calc.devision(a,b)
        # 判断用例是否通过
        self.assertEqual(s,c)



# 加载所有用例                                     # 第三步
tests = unittest.defaultTestLoader.discover(r"D:\day08\day13【单元测试】\代码\day13",pattern="main1.py")


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


'''
    1.准备数据，期望结果
    2.执行用例，调用add方法，传入数据，得到实际结果
    3.比对实际结果与期望结果是否一致，不一致提交bug.
'''
# # 准备数据
# a = 6
# b = 5
# c = 11
#
# calc = Calc()
#
# s = calc.add(a,b)
#
# # 判断用例是否通过
# if s == c:
#     print("用例通过！")
# else:
#     print("用例不通过！")























