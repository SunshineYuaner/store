# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/25 17:32
# 文件名：苏宁登录.py
# 开发工具：PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(6)

wd.get("https://passport.suning.com/login")
wd.maximize_window()

# 点击账户登录
wd.find_element(By.XPATH,"//*[@class='tab-item']").click()

# 输入账户
wd.find_element(By.XPATH,"//*[@id='userName']").send_keys("17671214525")

# 输入密码
wd.find_element(By.XPATH,"//*[@id='password']").send_keys("Hw000727")

# 点击按钮验证
wd.find_element(By.XPATH,'//*[@id="iar1_sncaptcha_button"]').click()

time.sleep(3)

# 点击登录
wd.find_element(By.XPATH,'//*[@id="submit"]').click()