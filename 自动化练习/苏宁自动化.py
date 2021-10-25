# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/22 14:25
# 文件名：苏宁自动化.py
# 开发工具：PyCharm




from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("https://suning.com")

# 搜索手机
wd.find_element(By.XPATH,"//*[@id='searchKeywords']").send_keys("iphone 12 pro max\n")

# 点击手机进入详情
wd.find_element(By.XPATH,"//*[@class='ltrbl']").click()

# 进入详情页面
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是需要操作的窗口
    if "三星手机" in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该窗口，正好跳出循环
        break

# 选择制式
wd.find_element(By.XPATH,"//*[@colorid='10012']").click()

# 选择颜色
wd.find_element(By.XPATH,"//*[@versionid='20003']").click()

# 支付定金
wd.find_element(By.XPATH,"//*[@id='addCart']").click()