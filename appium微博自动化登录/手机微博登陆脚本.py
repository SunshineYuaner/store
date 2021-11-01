import time

from appium import webdriver

data = {
  "deviceName": "vivo X27 Pro",
  "platformName": "Android",
  "platformVersion": "10",
  "appPackage": "com.sina.weibo",
  "appActivity": ".SplashActivity",
  "skipServerInstallation": True,
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",data)

# 弹窗广告
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]").click()
time.sleep(3)
# 系统权限设置
el2 = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
time.sleep(1)
# 点击登录
el3 = driver.find_element_by_id("com.sina.weibo:id/titleBack").click()
time.sleep(1)
# 点击同意协议
el4 = driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol").click()
time.sleep(1)
# 点击其他手机登录
el5 = driver.find_element_by_id("com.sina.weibo:id/btn_for_sms_login").click()
time.sleep(1)
# 点击选择账号密码登录
el6 = driver.find_element_by_id("com.sina.weibo:id/iv_psw").click()
time.sleep(1)
# 输入账号
el7 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_uname").send_keys("17671214523")
time.sleep(0.5)
# 输入密码
el8 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw").send_keys("Hw000727.")
time.sleep(0.5)
# 点击登录
el9 = driver.find_element_by_id("com.sina.weibo:id/btn_login_view_psw").click()
time.sleep(3)