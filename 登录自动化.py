from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 打开浏览器

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(service=Service(r'C:\tools\chromedriver.exe'))
# 创建环境变量后使用以下方法即可不用指定浏览器驱动
wd = webdriver.Chrome()
wd.implicitly_wait(10)
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('http://127.0.0.1:5500/page/login/login.html')

element = wd.find_element(By.ID, 'login-username')
element.send_keys('zjl')
element = wd.find_element(By.ID, 'login-password')
element.send_keys('123')
yzm_text = wd.find_element(By.ID, 'yzm').text
print("当前登录的验证码为：", yzm_text)
element = wd.find_element(By.ID, 'loginCaptchaInput')
element.send_keys(yzm_text)
dl_button = wd.find_element(By.ID, 'dl')
dl_button.click()

input('等待回车结束')
