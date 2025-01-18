# 单选元素与循环返回所有选中的元素

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('http://127.0.0.1:5500/page/login/login.html')

animal_element = wd.find_element(By.CLASS_NAME, 'form-group')

print(animal_element.text)

div_elements = wd.find_elements(By.TAG_NAME, 'div')

for span in div_elements:
    print(span.text)
