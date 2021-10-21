from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
# ActionChains 滑动滑块        ActionChains是一种自动化低级交互的方法，比如鼠标移动、鼠标按钮操作、按键和上下文菜单交互

wd = webdriver.Chrome()

wd.get("file:///D:/Users/87306/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E5%AE%89%E8%A3%85/%E7%BB%83%E4%B9%A0%E7%9A%84html"
       "/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E6%BB%91%E5%8A%A8%E9%AA%8C%E8%AF%81/mousedrag.html")

element = wd.find_element(By.CLASS_NAME,"slider")
action = ActionChains(wd)
action.click_and_hold(element)    # 按住
action.move_by_offset(248, 0)    # 往右偏移248个像素
action.release()                 # 释放鼠标
action.perform()                 # 执行