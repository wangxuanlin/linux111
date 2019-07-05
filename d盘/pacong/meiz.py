import requests
from lxml import etree

# 1 请求妹子图拿到网站数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'Referer': 'https://www.mzitu.com/tag/ugirls/'
}
response = requests.get("https://www.mzitu.com/tag/ugirls/", headers=headers)
xml = etree.HTML(response.text)

# 2.抽取图片标题、图片链接

alt_list = xml.xpath('//img[@class="lazy"]/@alt')
src_list = xml.xpath('//img[@class="lazy"]/@data-original')
for alt, src in zip(alt_list, src_list):
    # 3、下载图片
    response = requests.get(src, headers=headers)

    # 4、保存图片
    fileName = "tupian\\" + alt + '.jpg'
    print('正在保存图片文件：' + fileName)
    with open(fileName, 'wb') as f:
        f.write(response.content)
