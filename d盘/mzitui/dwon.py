import json
from mzhi import get_response

from lxml import etree

import os
from time import sleep


def read_json_file(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
        print(data)
    return data

def judge_file(filename):
    try:
        with open(filename) as f:
            pass
        return True
    except:
        return False

def create_dictionary(name):
    try:
        os.mkdir(name)
    except Exception as e:
        print(e)


def download_picture(name, url):
    headers = {
        'Referer': 'Referer: https://www.mzitu.com/183109',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    filemane = 'meinv/' + name + '/' + name + url[-8:]
    judge = judge_file(filemane)
    if judge:
        print('文件{}已存在'.format(filemane))
    else:
        img_content = get_response(url, headers=headers).content
        try:
            with open(filemane, 'wb') as f:
                f.write(img_content)
                sleep(0.5)
        except Exception as e:
            print(e)


def down_load_picture(name, url):
    response = get_response(url)
    html = etree.HTML(response.text)

    img_urls = html.xpath('//div[@class="main-image"]//img/@src')[0]

    download_picture(name, url=img_urls)

    try:
        next_page_url = html.xpath('//a[./span/text()="下一页»"]/@href')[0]
        while next_page_url:
            print(next_page_url)
            response = get_response(next_page_url)
            html = etree.HTML(response.text)
            img_urls = html.xpath('//div[@class="main-image"]//img/@src')[0]
            download_picture(name, url=img_urls)
            next_page_url = html.xpath('//a[./span/text()="下一页»"]/@href')[0]


    except Exception as e:
        print(e, '该套图保存结束')


def run():
    data = read_json_file(filename='mztui.json')

    create_dictionary(name='meinv')

    for d in data:
        create_dictionary(name='meinv/' + d['name'])
        down_load_picture(name=d['name'], url=d['url'])
        print(d)


if __name__ == '__main__':
    run()
