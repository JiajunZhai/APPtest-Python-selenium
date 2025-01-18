from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

# 指定浏览器
wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.implicitly_wait(10)

# 打开网页
wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID, 'kw')

# print(element.get_attribute('placeholder'))
# 打印元素内的隐性内容

element.send_keys('翟嘉俊')
print(element.get_attribute('value'))
# 打印输入框的内容

wd.quit()
