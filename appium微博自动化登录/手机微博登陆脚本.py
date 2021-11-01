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

time.sleep(8)
el1 = driver.find_element_by_id("com.sina.weibo:id/titleBack")
el1.click()
# el2 = driver.find_element_by_id("com.sina.weibo:id/btn_change_account")
# el2.click()
el3 = driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol")
el3.click()
el4 = driver.find_element_by_id("com.sina.weibo:id/btn_for_sms_login")
el4.click()
el5 = driver.find_element_by_id("com.sina.weibo:id/iv_psw")
el5.click()
el6 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_uname")
el6.send_keys("17671214523")
el7 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw")
el7.send_keys("Hw000727.")
el8 = driver.find_element_by_id("com.sina.weibo:id/btn_login_view_psw")
el8.click()