# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/21 15:19
# 文件名：跳转页面.py
# 开发工具：PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get(
    "file:///D:/Users/87306/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E5%AE%89%E8%A3%85/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E7"
    "%BB%83%E4%B9%A0%E7%9A%84html/%E8%B7%B3%E8%BD%AC%E9%A1%B5%E9%9D%A2/pop.html")
# 当前页面
# mainWindow 变量保存当前窗口的句柄
mainWindow = wd.current_window_handle
link = wd.find_element(By.ID, "goo").click()

# windows_handles属性:包括了当前浏览器里面所有的的窗口句柄
# 跳转页面
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是需要操作的窗口
    if "百度" in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该窗口，正好跳出循环
        break

# wd.title属性是当前窗口的标题栏 文本
print(wd.title)

wd.find_element(By.ID,"kw").send_keys("黄潍\n")

# 切换回保存之间的窗口
wd.switch_to.window(mainWindow)
print(wd.title)