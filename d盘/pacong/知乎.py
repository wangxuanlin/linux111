from selenium import webdriver
from lxml import etree



zhihu = webdriver.Chrome("/Users/admin/Downloads/chromedriver 2")
zhihu.get("https://www.zhihu.com/signin?next=%2F")
html = zhihu.page_source
xml = etree.HTML(html)

print(xml)
zhihu.quit()