# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/25 17:46
# 文件名：Bili登录.py
# 开发工具：PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://passport.bilibili.com/login")
wd.maximize_window()

# 输入账号
wd.find_element(By.XPATH,'//*[@id="login-username"]').send_keys("17671214523")

# 输入密码
wd.find_element(By.XPATH,'//*[@id="login-passwd"]').send_keys("Hw000727.")

# 点击登录
wd.find_element(By.XPATH,'//*[@class="btn btn-login"]').click()
time.sleep(8)

# 搜索鬼畜视频
wd.find_element(By.XPATH,'//*[@autocomplete="off"]').send_keys("改革春风吹满地\n")

for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if "改革春风吹满地" in wd.title:
        break

# 点击观看视频
wd.find_element(By.XPATH,'//*[@src="//i1.hdslb.com/bfs/archive/d52994a1876d07a975dc6683b78a898d9b581208.png@400w_250h_1c.webp"]').click()

for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if "春晚鬼畜" in wd.title:
        break

# 点击全屏观看
wd.find_element(By.XPATH,'//*[@id="图层_1"]').click()