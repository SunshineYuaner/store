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
driver.implicitly_wait(8)

# 弹窗广告
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]").click()

# 系统权限设置
el2 = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()

# 点击登录
el3 = driver.find_element_by_id("com.sina.weibo:id/titleBack").click()

# 点击同意协议
el4 = driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol").click()

# 点击其他手机登录
el5 = driver.find_element_by_id("com.sina.weibo:id/btn_for_sms_login").click()

# 点击选择账号密码登录
el6 = driver.find_element_by_id("com.sina.weibo:id/iv_psw").click()

# 输入账号
el7 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_uname").send_keys("17671214523")

# 输入密码
el8 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw").send_keys("Hw000727.")

# 点击登录
el9 = driver.find_element_by_id("com.sina.weibo:id/btn_login_view_psw").click()

# 点击搜索
el10 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='发现']").click()

# 取消定位
el11 = driver.find_element_by_id("com.sina.weibo:id/btn_close").click()

# 点击搜索框
el12 = driver.find_element_by_id("com.sina.weibo:id/tv_search_keyword").click()

# 搜索EDG
el13 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.EditText").send_keys("EDG")

# 点击第一条热搜
el14 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout").click()

# 点击EDG进入官博
el15 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ListView/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView[2]").click()

# 点击微博
el16 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView").click()

# 点击第一篇文章
el17 = driver.find_element_by_id("com.sina.weibo:id/contentTextView").click()