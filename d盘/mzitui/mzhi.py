import requests
from lxml import etree
from time import sleep
import json


def get_response(url,headers=None):
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko'}
    response = requests.get(url, headers=headers)
    return response
    # if response.status_code == 200:
    #      return response
    # else:
    #     raise EnvironmentError


def parse_htmll(response):
    html = etree.HTML(response.text)

    page_imag_urls = []

    page_img_content = html.xpath('//div[@class="postlist"]//ul//li')
    for img in page_img_content:
        img_info = {}

        img_info['name'] = img.xpath('./a[1]/img/@alt')[0]

        img_info['url'] = img.xpath('./a[1]/@href')[0]
        page_imag_urls.append(img_info)
    print(page_imag_urls)
    return page_imag_urls

def get_next_url(response):

    html = etree.HTML(response.text)
    next_urls = html.xpath('//a[text()="下一页»"]/@href')

    if len(next_urls)>0:
        return next_urls[0]
    else:
        return None


def save_to_file(filename, data):
    data = json.dumps(data)
    filename = filename+'.json'
    with open(filename,'w') as f:
        print('正在保存{}'.format(filename))
        f.write(data)
    print('保存完成')





def run():

    index_urls = ['https://www.mzitu.com/tag/youhuo/','https://www.mzitu.com/japan/','https://www.mzitu.com/taiwan/','https://www.mzitu.com/mm/','']
    index_url = 'https://www.mzitu.com/tag/youhuo/'

    all_img_info = []

    response = get_response(index_url)

    all_img_info.extend(parse_htmll(response))

    parse_htmll(response)

    next_urls = get_next_url(response)

    while next_urls:

        print(next_urls)

        sleep(2)

        response = get_response(next_urls)

        all_img_info.extend(parse_htmll(response))

        parse_htmll(response)

        next_urls = get_next_url(response)

    print('爬取完成，共{}条数据'.format(len(all_img_info)))

    save_to_file(filename='mztui', data=all_img_info)








if __name__ == '__main__':
    run()

