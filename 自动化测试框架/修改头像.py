# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/28 17:24
# 文件名：修改头像.py
# 开发工具：PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get("http://localhost:8080/HKR")
wd.maximize_window()

# 输入用户名
wd.find_element(By.XPATH,"//*[@id='loginname']").send_keys("yuaner")

# 输入密码
wd.find_element(By.XPATH,"//*[@id='password']").send_keys("Hw000727.")

# 点击登录
wd.find_element(By.XPATH,"//*[@id='submit']").click()

# 点击更换头像
wd.find_element(By.XPATH,"//*[@id='img']").click()

# 点击选择图片
wd.find_element(By.XPATH,"//*[@id='filename']").send_keys(r"D\壁纸\111.jpg")

