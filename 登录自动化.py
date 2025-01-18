from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
# 用于捕获 NoSuchElementException 异常并输出“登录失败”
from time import sleep

# 打开浏览器

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(service=Service(r'C:\tools\chromedriver.exe'))
# 创建环境变量后使用以下方法即可不用指定浏览器驱动
wd = webdriver.Chrome()
wd.implicitly_wait(5)
# 全局等待5s
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('http://127.0.0.1:5500/page/login/login.html')

username = 'qq'
password = 'qq'


wd.find_element(By.ID, 'login-username').send_keys(username)
wd.find_element(By.ID, 'login-password').send_keys(password)

# 自动获取验证码
# yzm_text = wd.find_element(By.ID, 'yzm').text
# print("当前登录的验证码为：", yzm_text)
element = wd.find_element(By.ID, 'loginCaptchaInput')
# element.send_keys(yzm_text)
dl_button = wd.find_element(By.ID, 'dl')
dl_button.click()
# 假设登录成功后会显示一个带有用户名字的元素
try:
    user_element = wd.find_element(By.ID, 'username-value')
    user_name = user_element.text
    print("登录成功", user_name)
except NoSuchElementException:
    print("登录失败")
