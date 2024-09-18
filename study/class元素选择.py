# 单选元素与循环返回所有选中的元素

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

animal_element = wd.find_element(By.CLASS_NAME, 'animal')

print(animal_element.text)

div_elements = wd.find_elements(By.TAG_NAME, 'div')

for span in div_elements:
    print(span.text)
