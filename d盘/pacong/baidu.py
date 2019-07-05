from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")
print(driver.page_source)
driver.close()