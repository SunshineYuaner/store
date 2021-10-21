from selenium import webdriver

wd = webdriver.Chrome()

wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')

# 切换到frame框里面
# wd.switch_to.frame("frame1")
# 可以根据frame的元素位置或者属性特性，使用find系列的方法，选择到该元素
wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))
# 根据 class name 选择元素，返回的是 一个列表
elements = wd.find_elements_by_class_name('plant')

for element in elements:
    print(element.text)

# 切换回 最外部的 HTML 中
wd.switch_to.default_content()

# 然后再 选择操作 外部的 HTML 中 的元素
wd.find_element_by_id('outerbutton').click()

wd.quit()
