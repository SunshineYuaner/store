# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/22 14:40
# 文件名：淘宝登录.py
# 开发工具：PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

wd = webdriver.Chrome()
wd.implicitly_wait(5)

# 进入淘宝页面
wd.get("https://taobao.com")
wd.maximize_window()

# 点击登录按钮
wd.find_element(By.XPATH,"//*[@class='h']").click()

# 输入账号
wd.find_element(By.XPATH,"//*[@name='fm-login-id']").send_keys("111")

# 输入密码
wd.find_element(By.XPATH,"//*[@name='fm-login-password']").send_keys("111")
time.sleep(5)

# # 滑动
# element = wd.find_element(By.XPATH,"//*[@id='nc_1_n1z']")
# action = ActionChains(wd)
# action.click_and_hold(element)    # 按住
# action.move_by_offset(258, 0)    # 往右偏移258个像素
# action.release()                 # 释放鼠标
# action.perform()                 # 执行

# 点击登录
wd.find_element(By.XPATH,"//*[@class='fm-button']").click()







