from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get("file:///D:/Users/87306/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E5%AE%89%E8%A3%85/%E7%BB%83%E4%B9%A0%E7%9A%84html"
       "/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E5%BC%B9%E6%A1%86%E7%9A%84%E9%AA%8C%E8%AF%81/dialogs.html")
# # 基础弹出框
# # 点击按钮弹出对话框
# wd.find_element(By.ID,"alert").click()
#
# # 打印 弹出框 提示信息
# print(wd.switch_to.alert.text)
#
# # 点击 确认 按钮
# wd.switch_to.alert.accept()


# 用户确认弹出框
# # 点击按钮弹出对话框
# wd.find_element(By.ID,"confirm").click()
#
# # 打印 弹出框 提示信息
# print(wd.switch_to.alert.text)
#
# # 点击 确定 按钮
# wd.switch_to.alert.accept()
#
# wd.find_element(By.ID,"confirm").click()
#
# # 点击取消按钮
# wd.switch_to.alert.dismiss()





# 弹出框 需要 输入信息，在确定或取消
wd.find_element(By.ID,"confirm").click()

# 输入信息
wd.switch_to.alert.send_keys("黄潍爱杜圆")
# 点击确定
wd.switch_to.alert.accept()

wd.find_element(By.ID,"confirm").click()

# 打印 弹出框 提示信息
print(wd.switch_to.alert.text)

# 点击 确定 按钮
wd.switch_to.alert.accept()

wd.find_element(By.ID,"confirm").click()

# 点击取消按钮
wd.switch_to.alert.dismiss()
