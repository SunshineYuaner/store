from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("D:/Users/87306/Desktop/自动化安装/练习的html/练习的html/上传文件和下拉列表/autotest.html")

# Select的模块，供处理下拉菜单
element = wd.find_element(By.CLASS_NAME,"u17")
Select(element).select_by_index(1)