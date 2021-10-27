# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/25 17:04
# 文件名：京东登录.py
# 开发工具：PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(6)

wd.get("https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F")
wd.maximize_window()

# 选择账户登录
wd.find_element(By.XPATH,"//*[@clstag='pageclick|keycount|login_pc_201804112|10']").click()

# 输入账户
wd.find_element(By.XPATH,"//*[@id='loginname']").send_keys("17671214525")

# 输入密码
wd.find_element(By.XPATH,'//*[@id="nloginpwd"]').send_keys("Hw000727")

# 点击登录
wd.find_element(By.XPATH,'//*[@id="loginsubmit"]').click()

