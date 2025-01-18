from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.implicitly_wait(10)

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')

element = wd.find_element(By.ID, 'outerbutton')
element.click()

# 切换到frame元素内
wd.switch_to.frame('frame1')

# 根据 class name 选择元素，返回的是 一个列表
elements = wd.find_elements(By.CLASS_NAME, 'plant')

for element in elements:
    print(element.text)

# 切换回 最外部的 HTML 中
wd.switch_to.default_content()
# 对外部按钮进行操作
element = wd.find_element(By.ID, 'outerbutton')
element.click()

input('6')
