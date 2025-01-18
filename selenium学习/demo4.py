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

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys('通讯')

element = wd.find_element(By.ID, 'go')
element.click()

# sleep(1)

# while True:
#     try:
#         element = wd.find_element(By.ID, '1')
#         print(element.text)
#         break
#     except:
#         sleep(1)
element = wd.find_element(By.ID, '1')
print(element.text)

wd.quit()
