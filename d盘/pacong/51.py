from selenium import webdriver
from lxml import etree

driver = webdriver.Chrome('/Users/admin/Downloads/chromedriver 2')
# driver.fullscreen_window()
driver.get('https://www.51job.com/')
driver.find_element_by_id('kwdselectid').send_keys('python 爬虫\n')
html = driver.page_source
xml = etree.HTML(html)
titles = xml.xpath('//p[@class="t1 "]/span/a/@title')
companys = xml.xpath('//span[@class="t2"]/a/@title')
wages = xml.xpath('//div[@class="el"]/span[@class="t4"]')
for i, a, z in zip(titles, companys, wages):
    print(i, a, z.text)

