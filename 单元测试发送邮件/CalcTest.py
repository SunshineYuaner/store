'''
    unittest:单元测试
    1.子类继承unittest.TestCase
    2.写测试用例：testXxxxx
'''
from unittest import TestCase
from Calc import Calc
class CalcTest(TestCase):

    def testAdd1(self):
        a = -6
        b = 5
        c = 11

        calc = Calc()
        s = calc.add(a,b)

        # 判断用例是否通过
        self.assertEqual(s,c)


    def testAdd2(self):
        a = -6
        b = -5
        c = -11

        calc = Calc()
        s = calc.add(a,b)

        # 判断用例是否通过
        self.assertEqual(s,c)

    def testAdd3(self):
        a = -6
        b = 5
        c = -1

        calc = Calc()
        s = calc.add(a,b)

        # 判断用例是否通过
        self.assertEqual(s,c)


    def testAdd4(self):
        a = 9
        b = -5
        c = 4

        calc = Calc()
        s = calc.add(a,b)

        # 判断用例是否通过
        self.assertEqual(s,c)



    def testAdd5(self):
        a = 900000000000000000000000000000000000000000000000000000000000000000000000
        b = 5
        c = 900000000000000000000000000000000000000000000000000000000000000000000005

        calc = Calc()
        s = calc.add(a,b)

        # 判断用例是否通过
        self.assertEqual(s,c)


    def testAdd6(self):
        a = 0
        b = 5
        c = 5

        calc = Calc()
        s = calc.add(a,b)

        # 判断用例是否通过
        self.assertEqual(s,c)




    def testAdd7(self):
        a = 0
        b = -5
        c = -5

        calc = Calc()
        s = calc.add(a,b)

        # 判断用例是否通过
        self.assertEqual(s,c)















