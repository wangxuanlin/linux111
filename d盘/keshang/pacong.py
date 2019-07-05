import requests
from bs4 import BeautifulSoup
# res = requests.get(url="http://blog.jobbole.com/114694/")
# soup = BeautifulSoup(res.text)
#
# print(res.text)

crawled_list = set()
def get(url):
    crawled_list.add(url)
    print("-------")
    print(crawled_list)
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text)
    return soup

def start(url):
    if url in crawled_list:
        return
    res = get(url)
    print('文章标题{}'.format(res.select('div.entry-header h1')[0].text))
    a_list = res.select('li span.digg-item-updated-title a')
    for a in a_list:
        href = a.attrs['href']
        run(href)



def run(href):
    if href in crawled_list:
        return
    res = get(href)
    print('文章标题{}'.format(res.select('div.entry-header h1')[0].text))

    a_lists = res.select('li span.digg-item-updated-title a')
    for a in a_lists:
        href = a.attrs['href']
        run(href)


if __name__ == "__main__":
    start("http://blog.jobbole.com/114694/")
