# _*_ coding:utf-8 _*_
# 开发人员：Sunshine、Yuaner
# QQ：873064448
# 开发时间：2021/10/22 10:28
# 文件名：京东自动化.py
# 开发工具：PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

# 进入京东
wd.get("https://jd.com")

# 搜索苹果
wd.find_element(By.XPATH,"//*[@id='key']").send_keys("iphone 13 pro max\n")

# 点击手机进图购买页面
wd.find_element(By.XPATH,"//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()

# 跳转到购买页面
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是需要操作的窗口
    if "远峰蓝色" in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该窗口，正好跳出循环
        break

# 选择颜色
wd.find_element(By.XPATH,"//*[@data-sku='10037903424429']").click()

# 选择版本
wd.find_element(By.XPATH,"//*[@data-sku='10037903424432']").click()

# 加入购物车
element = wd.find_element(By.XPATH,"//*[@id='InitCartUrl']")
wd.execute_script("arguments[0].click();", element)
