from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://www.byhy.net/_files/stock1.html')

try:
    element = wd.find_element(By.ID, 'kww')
    element.send_keys('通讯\n')
    element = wd.find_element(By.ID, '1')
    print(element.text)
    pass
except NoSuchElementException:
    print('元素不存在')
    pass


