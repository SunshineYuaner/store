import time


class LoginOperation:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, pwd):
        # 弹窗广告
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]").click()
        time.sleep(3)
        # 系统权限设置
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        time.sleep(1)
        # 点击登录
        self.driver.find_element_by_id("com.sina.weibo:id/titleBack").click()
        time.sleep(1)
        # el2 = driver.find_element_by_id("com.sina.weibo:id/btn_change_account")
        # el2.click()
        # 点击同意协议
        self.driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol").click()
        time.sleep(1)
        # 点击其他手机登录
        self.driver.find_element_by_id("com.sina.weibo:id/btn_for_sms_login").click()
        time.sleep(1)
        # 点击选择账号密码登录
        self.driver.find_element_by_id("com.sina.weibo:id/iv_psw").click()
        time.sleep(1)
        # 输入账号
        self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_uname").send_keys(username)
        time.sleep(0.5)
        # 输入密码
        self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw").send_keys(pwd)
        time.sleep(0.5)
        # 点击登录
        self.driver.find_element_by_id("com.sina.weibo:id/btn_login_view_psw").click()
        time.sleep(3)

    def getSuccess_result(self):
        return self.driver.find_element_by_id("com.sina.weibo:id/contentTextView").text
    def getError_result(self):
        return self.driver.find_element_by_id("com.sina.weibo:id/tv_login_view_tips").text
