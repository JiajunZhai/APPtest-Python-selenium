from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.implicitly_wait(10)

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com/')

link = wd.find_element(By.CLASS_NAME, 'title-content-title')
link.click()

sleep(1)

print(wd.title)

# 进入的窗口
mainWindow = wd.current_window_handle

for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if '携手' in wd.title:
        break
print(wd.title)

# 选择窗口
wd.switch_to.window(mainWindow)

print(wd.title)

element = wd.find_element(By.ID, 'kw')
element.send_keys('我在百度')
print(element.get_attribute('value'))

wd.quit()
