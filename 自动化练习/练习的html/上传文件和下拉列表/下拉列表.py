from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("D:/Users/87306/Desktop/自动化安装/练习的html/练习的html/上传文件和下拉列表/autotest.html")

# 输入用户名与密码
wd.find_element(By.XPATH,"//*[@name='account']").send_keys("111")
wd.find_element(By.XPATH,"//*[@name='password']").send_keys("222")

# 选择地区                  Select的模块，供处理下拉菜单
element = wd.find_element(By.CLASS_NAME,"u17")
Select(element).select_by_index(1)

# 点击性别
wd.find_element(By.XPATH,"//*[@id='sexID2']").click()

# 点击季节
wd.find_element(By.XPATH,"//*[@value='summer']").click()

# 上传文件
wd.find_element(By.XPATH,"//*[@name='file' and @type='file']").send_keys(r"D:\壁纸\111.jpg")


