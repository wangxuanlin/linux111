import requests
from lxml import etree
import pymysql

headers = {
    'Referer': 'https://www.zhipin.com/c101270100-p100109/?page=2&ka=page-2',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
response = requests.get('https://www.zhipin.com/c101270100-p100109/?page=2&ka=page-2', headers=headers)
xml = etree.HTML(response.text)

titles = xml.xpath('//div[@class="job-title"]')
reds = xml.xpath('//span[@class="red"]')

for title,red in zip(titles, reds):
    print(title.text, red.text)