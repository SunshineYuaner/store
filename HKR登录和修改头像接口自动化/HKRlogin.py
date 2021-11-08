'''
    1.requests模块
        联网安装这个模块
    2.导入这个模块
    3.requests来请求接口并得到响应数据
    4.判断响应数据中是否包含我们期望 的数据

    任务1：修改头像的接口使用接口自动化做一遍？
'''
from unittest import TestCase
import requests
class TestHkrLogin(TestCase):

    def testLogin1(self):
        # 准备数据
        data = {
            "method":"login",
            "loginname":"admin",
            "password":"root"
        }
        expect = "菜单"

        # 使用requests发送请求
        response = requests.post(url="http://localhost:8080/HKR/UserServlet",data=data)
        # 提取响应状态吗
        code = response.status_code
        response.encoding = "utf-8"

        # 提取响应体
        text = response.text

        f = open(file="登陆.html",mode="w+",encoding="utf-8")
        f.write(text)
        f.flush()
        if code == 200 and text.__contains__(expect):
            print("用例通过！")
        else:
            print("用例失败！")


    def testLogin2(self):
            # 准备数据
            data = {
                "method":"login",
                "loginname":"yuaner",
                "password":"Hw000727."
            }
            expect = "菜单"

            # 使用requests发送请求
            response = requests.post(url="http://localhost:8080/HKR/UserServlet",data=data)
            # 提取响应状态吗
            code = response.status_code
            response.encoding = "utf-8"

            # 提取响应体
            text = response.text

            f = open(file="登陆.html",mode="w+",encoding="utf-8")
            f.write(text)
            f.flush()
            if code == 200 and text.__contains__(expect):
                print("用例通过！")
            else:
                print("用例失败！")







