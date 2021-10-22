'''
    测试银行：
        使用参数化。
        测试银行的核心业务
'''
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack

 #1.开户
from Bank import bank_addUser
#username, password, country, province, street, door, money
da = [
    ["jason","123456","cn","安徽省","桃源路","s001",6000,1],#99
    ["jason","123456","cn","安徽省","桃源路","s001",6000,2],#重复
    ["jaso","123456","cn","安徽省","桃源路","s001",6000,1],#100
    ["jas","123456","cn","安徽省","桃源路","s001",6000,3]#101，已满
]
@ddt
class TestBank(TestCase):
    for i in range(98):
        name="jason"+str(i)
        bank_addUser(name,"123456","cn","安徽省","桃源路","s001",6000)
    @data(*da)
    @unpack
    def testAddUser(self,a,b,c,d,e,f,g,h):
        result = bank_addUser(a,b,c,d,e,f,g)
        self.assertEqual(result,h)

##2.存钱
from Bank import bank_saveMoney
da_cq = [["00000000",0,True],#0
         ["00000000",1,True],#1
         ["00000000",-1,False],#-1
         ["00000001",1,False],#账号错误
         ["00000000",100000000000000000000,True],#额数大
         ["",1,False]#账号空
]
@ddt
class cq(TestCase):
    @data(*da_cq)
    @unpack
    def testsaveMoney(self,a,b,c):
        result = bank_saveMoney(a,b)
        self.assertEqual(result,c)

#3.取钱
from Bank import bank_takeMoney
da_qq = [["00000000","123456",-1,3],#-1
         ["00000000","123456",0,0],#0
         ["00000000","123456",1,0],#1
         ["11111111","123456",599,0],#599
         ["22222222","123456",600,0],#600
         ["33333333","123456",601,3],#601
         ["00000001","123456",1,1],#账号不对
         ["00000000","123",1,2],#密码不对
         ["00000001","123",1,1],#账号密码不对
         ["","123456",1,1],#账号空
         ["00000000","",1,2],#密码空
         ["","",1,1],#账号密码空
]
@ddt
class qq(TestCase):
    @data(*da_qq)
    @unpack
    def testtakeMoney(self,a,b,c,d):
        result = bank_takeMoney(a,b,c)
        self.assertEqual(result,d)

#4.转账
from Bank import bank_transformMoney
da_zz = [
["00000000","11111111","123456",-1,3],#-1
["00000000","11111111","123456",0,0],#0
["00000000","11111111","123456",1,0],#1
["22222222","11111111","123456",599,0],#599
["33333333","11111111","123456",600,0],#600
["44444444","11111111","123456",601,3],#601
["00000001","11111111","123456",1,1],#转出账号不对
["00000000","11111111","12345",1,2],#转出密码不对
["00000000","11111110","123456",1,1],#转入账号不对
["00000001","11111110","123456",1,1],#转出账号，转入账号不对
["00000001","11111111","12345",1,1],#转出账号，转出密码不对
["00000000","11111111","12345",1,1],#转入账号，转出密码不对
["00000001","11111110","12345",1,1],#转出账号，转入账号转出密码不对
["00000000","","123456",1,1],#转入账号空
["","11111111","123456",1,1],#转出账号空
["00000000","11111111","",1,2],#转出密码空
["","11111111","",1,1],#转出账号，转出密码空
["00000000","","",1,1],#转出账号，转出密码空
["","","123456",1,1],#转出账号，转入账号空
["","","",1,1]#转出账号，转出密码，转入账号空
]
@ddt
class zz(TestCase):
    @data(*da_zz)
    @unpack
    def testtransformMoney(self,a,b,c,d,e):
        result = bank_transformMoney(a,b,c,d)
        self.assertEqual(result,e)

