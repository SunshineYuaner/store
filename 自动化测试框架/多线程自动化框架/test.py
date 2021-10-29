from threading import Thread
from HTMLTestRunner import HTMLTestRunner
import unittest
import os


class execute(Thread):
    def __init__(self, test_file, html_file):
        super().__init__()
        self.test_file = test_file
        self.html_file = html_file

    def run(self) -> None:
        runner = HTMLTestRunner.HTMLTestRunner(
            title="用例测试报告",
            description="测试详细报告",
            verbosity=1,
            stream=open(f'{self.html_file}', mode="w+", encoding="utf-8")
        )
        runner.run(unittest.defaultTestLoader.discover(os.getcwd(), pattern=f'{self.test_file}'))


if __name__ == '__main__':
    login_s = execute('testnormal.py', '用例成功报告.html')
    login_f = execute('testerror.py', '用例失败报告.html')
    login_f.start()
    login_s.start()
    login_s.join()
    login_f.join()
