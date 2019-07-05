import requests
import ssl

from bs4 import BeautifulSoup
import urllib.request


def meizi():
    ssl._create_default_https_context = ssl._create_unverified_context
    heads = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    response = requests.get('https://movie.douban.com/', headers=heads)
    print(response)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    meiz = soup.find_all('img')
    x = 0
    for i in meiz:
        img = i.get('src')
        # img1 = urllib.request.Request(img,headers=heads)
        print(img)
        urllib.request.urlretrieve(img)
        x += 1
        print('正在下载{}张'.format(x))




meizi()