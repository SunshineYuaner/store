from unittest import TestCase
import requests


class TestHkrPicture(TestCase):

    def testHkrPicture1(self):
        # 准备数据
        data = {
           "pid": "afda484fda8dfag84af8da84a8df4a",
           "uid": "45946a72abd8476fa60f80342c62e64b"
        }
        expect = "操作提示"

        # 使用requests发送请求
        response = requests.post(url="http://localhost:8080/HKR/UserServlet?method=changePicture", data=data)
        # 提取响应状态码
        code = response.status_code
        response.encoding = "utf-8"
        # 响应文本
        text = response.text

        if code == 200 and text.__contains__(expect):
            print("用例通过")
        else:
            print("用例失败")

    def testHkrPicture2(self):
        # 准备数据
        data = {
            "pid": "752248cbe5064ca294bcac1f108af691",
            "uid": "45946a72abd8476fa60f80342c62e64b"
        }
        expect = "操作提示"

        # 使用requests发送请求
        response = requests.post(url="http://localhost:8080/HKR/UserServlet?method=changePicture", data=data)
        # 提取响应状态码
        code = response.status_code
        response.encoding = "utf-8"
        # 响应文本
        text = response.text

        if code == 200 and text.__contains__(expect):
            print("用例通过")
        else:
            print("用例失败")
