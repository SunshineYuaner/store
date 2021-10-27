# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/25 20:03
# 文件名：知乎登录.py
# 开发工具：PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(6)

wd.get("https://zhihu.com")
wd.maximize_window()

# 选择密码登录
wd.find_element(By.XPATH,'//*[@class="SignFlow-tab"]').click()

# 输入账号
wd.find_element(By.XPATH,'//*[@placeholder="手机号或邮箱"]').send_keys("17671214523")

# 输入密码
wd.find_element(By.XPATH,'//*[@placeholder="密码"]').send_keys("Hw000727.")

# 点击登录
wd.find_element(By.XPATH,'//*[@type="submit"]').click()