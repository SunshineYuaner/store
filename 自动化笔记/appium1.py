from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'vivo X27 Pro', # 设备名，安卓手机可以随意填写
  'appPackage': 'tv.danmaku.bili', # 启动APP Package名称
  'appActivity': '.MainActivityV2', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法   再程序中调式时会终止神的来不及恢复，用处不大，可有可无，最后还得人工恢复
  'noReset': True,       # 不要重置App，非常重要
  'newCommandTimeout': 6000,  # 客户端链接操作时间，长一点方便一些
  'automationName' : 'UiAutomator2',
  "skipServerInstallation": True, # 当设备上没有uiautomator2包时，不能设置skipServerInstallation：True
  # 'skipServerInstallation': True,    当设备上没有uiautomator2包时，不能设置skipServerInstallation：True
  # 'skipDeviceInitialization': True
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# 如果有`青少年保护`界面，点击`我知道了`
iknow = driver.find_elements_by_id("text3")
if iknow:
    iknow.click()

# 根据id定位搜索位置框，点击
driver.find_element_by_id("expand_search").click()

# 根据id定位搜索输入框，点击
sbox = driver.find_element_by_id('search_src_text')
sbox.send_keys('')
# 输入回车键，确定搜索
driver.press_keycode(AndroidKey.ENTER)

# 选择（定位）所有视频标题
eles = driver.find_elements_by_id("title")

for ele in eles:
    # 打印标题
    print(ele.text)

input('**** Press to quit..')
driver.quit()



# pip install appiym-python-client


# 查找应用 Package 和 Activity
# 没有apk：cmd输入:   adb shell dumpsys activity recents | find "intent={"   查看cmp
# 有apk：查package名称：D:\androidsdk\build-tools\29.0.3\aapt.exe dump badging d:\apk\bili.apk(目标路径) | find "package: name="
#         查Activity信息：D:\androidsdk\build-tools\29.0.3\aapt.exe dump badging d:\apk\bili.apk(目标路径) | find "launchable-activity"
# 微信：com.tencent.mm/.ui.LauncherUI
# B站：tv.danmaku.bili/.MainActivityV2