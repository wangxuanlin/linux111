from selenium import webdriver
import time

from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path="/opt/bin/chromedriver")
driver.get("http://10.2.0.193:8000/exercises/spider/level4/")
time.sleep(1)
tag = driver.find_element_by_id("userinfo")
assert isinstance(tag, WebElement)
for t in tag.find_elements_by_tag_name("tr"):
    user_info = t.find_elements_by_tag_name("td")
    username = user_info[0].text
    age = user_info[1].text
    gender = user_info[2].text

    print(username, age, gender)
