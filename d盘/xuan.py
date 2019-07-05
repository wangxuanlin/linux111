from selenium import webdriver
import time

from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path='/Users/admin/Desktop/chromedriver')
driver.get('https://www.baidu.com/')
time.sleep(1)
tag = driver.find_element_by_class_name('s_ipt')
assert isinstance(tag,WebElement)
tag.send_keys('91秦先生')
time.sleep(3)
tag.submit()