from selenium import webdriver
import time


driver = webdriver.Chrome('/Users/admin/Downloads/chromedriver 2')
driver.fullscreen_window()
driver.get('https://www.baidu.com/')
driver.find_element_by_name('wd').send_keys('sb')
time.sleep(2)


driver.quit()

