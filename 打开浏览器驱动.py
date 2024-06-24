from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 打开浏览器

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(service=Service(r'C:\tools\chromedriver.exe'))
# 创建环境变量后使用以下方法即可不用指定浏览器驱动
wd = webdriver.Chrome()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

element = wd.find_element(By.ID, 'kw')

sleep(1)

element.send_keys('通讯\n')

sleep(3)

# 程序运行完会自动关闭浏览器，就是很多人说的闪退
# 这里加入等待用户输入，防止闪退
# input('等待回车键结束程序')
