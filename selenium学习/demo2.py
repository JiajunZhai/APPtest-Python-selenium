from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# 根据 class name 选择元素，返回的是 一个列表
# 里面 都是class 属性值为 animal的元素对应的 WebElement对象
elements = wd.find_elements(By.CLASS_NAME, 'animal')
# print(elements.text)

# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)

input('输入回车')
