# pip install selenium


# from selenium import webdriver                   id
# # 创建 WebDriver 对象，指明使用chrome浏览器驱动
# driver = webdriver.Chrome()
#
# # 调用WebDriver 对象的get方法，可以让浏览器打开指定网址
# driver.get("https://www.baidu.com")
#
# # 根据id选择元素，返回的就是该元素对应的WebElement对象
# element = driver.find_element_by_id("kw")
#
# # 通过该 WebElement 对象，就可以对页面元素进行操作了
# # 比如输入字符串到 这个 输入框里
# element.send_keys("黄潍\n")


# from selenium import webdriver                   class name
# # 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome()
#
# # WebDriver 实例对象的get方法 可以让浏览器打开指定网址
# wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
#
# # 根据 class name 选择元素，返回的是 一个列表
# # 里面 都是class 属性值为 animal的元素对应的 WebElement对象
# elements = wd.find_elements_by_class_name('animal')
#
# # 取出列表中的每个 WebElement对象，打印出其text属性的值
# # text属性就是该 WebElement对象对应的元素在网页中的文本内容
# for element in elements:
#     print(element.text)


# from selenium import webdriver                   tag name
# wd = webdriver.Chrome()
# wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
#
# # 根据 tag name 选择元素，返回的是 一个列表
# # 里面 都是 tag 名为 span 的元素对应的 WebElement对象
# elements = wd.find_elements_by_tag_name('span')
#
# # 取出列表中的每个 WebElement对象，打印出其text属性的值
# # text属性就是该 WebElement对象对应的元素在网页中的文本内容
# for element in elements:
#     print(element.text)


# from selenium import webdriver                      # WebDriver 对象 选择元素的范围是 整个 web页面， 而WebElement 对象 选择元素的范围是 该元素的内部。
# wd = webdriver.Chrome()
# wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
#
# element = wd.find_element_by_id('container')
#
# # 限制 选择元素的范围是 id 为 container 元素的内部。
# spans = element.find_elements_by_tag_name('span')
# for span in spans:
#     print(span.text)


# from selenium import webdriver            driver.implicitly_wait(10)设置隐式等待时间
# driver = webdriver.Chrome()
# driver.get("https://baidu.com")
# driver.implicitly_wait(10)
#
# element = driver.find_element_by_id("kw")
# element.send_keys("黄潍\n")
#
# # time.sleep(1)
# element = driver.find_element_by_id("1")
# print(element.text)


# from selenium import webdriver          #click()点击     get_attribute()获取属性  outerHTML获取整个元素对应的HTML  value获取输入的值
#                                         #quit()执行完自动关闭
# # 创建 WebDriver 对象，指明使用chrome浏览器驱动
# driver = webdriver.Chrome()
# # 调用WebDriver 对象的get方法，可以让浏览器打开指定网址
# driver.get("https://www.baidu.com")
# driver.implicitly_wait(8)
#
# # 根据id选择元素，返回的就是该元素对应的WebElement对象
# element = driver.find_element_by_id("kw")
#
# # 通过该 WebElement 对象，就可以对页面元素进行操作了
# # 比如输入字符串到 这个 输入框里
# element.send_keys("黄潍")
# driver.find_element_by_id("su").click()
#
# element = driver.find_element_by_id("1")
# # print(element.get_attribute("srcid"))
# print(element.get_attribute("outerHTML"))
# driver.quit()


# from selenium import webdriver
#
# #1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
# browser = webdriver.Chrome()
#
# #2.通过浏览器向服务器发送URL请求
# browser.get("https://www.baidu.com/")
#
#
# #3.刷新浏览器
# browser.refresh()
#
# #4.设置浏览器的大小
# browser.set_window_size(1400,800)
#
# #5.设置链接内容
# element=browser.find_element_by_link_text("新闻")
# element.click()
#
# element=browser.find_element_by_link_text("“下团组”时间")
# element.click()

# wd.text   获取整个页面文本     wd.title  获取页面标题

# 切换frame里面
# wd.switch_to.frame("iframe")
# wd.switch_to.frame(wd.find_element_by_css_selector('iframe[src="sample1.html]'))
# 切换frame外面
# wd.switch_to.default_content()

# 切换另一个窗口
# wd.switch_to.windows()
# for handle in wd.window_handles:
#     # 先切换到该窗口
#     wd.switch_to.window(handle)
#     # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
#     if 'Bing' in wd.title:
#         # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
#         break
# 切换回原来的窗口
# mainWindow变量保存当前窗口的句柄         mainWindow = wd.current_window_handle
#通过前面保存的原来的句柄，自己切换到原来窗口         wd.switch_to.window(mainWindow)

# 冻结界面          setTimeout(function(){debugger}, 5000)     5000指毫秒，表示在 5000毫秒后，执行 debugger 命令，执行该命令会 浏览器会进入debug状态。 debug状态有个特性， 界面被冻住， 不管我们怎么点击界面都不会触发事件。









