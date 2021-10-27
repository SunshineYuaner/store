# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/26 9:13
# 文件名：企查查登录.py
# 开发工具：PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://www.qcc.com")
wd.maximize_window()

# 点击登录/注册按钮
wd.find_element(By.XPATH,'//*[@class="navi-btn login-nav-btn"]').click()

# 选择密码登录
wd.find_element(By.XPATH,'//*[@id="normalLogin"]').click()

# 输入账号
wd.find_element(By.XPATH,'//*[@id="nameNormal"]').send_keys("111")

# 输入密码
wd.find_element(By.XPATH,'//*[@id="pwdNormal"]').send_keys("222222")

# 点击登录
wd.find_element(By.XPATH,'//*[@class="btn btn-primary btn-block m-t-lg login-btn"]').click()