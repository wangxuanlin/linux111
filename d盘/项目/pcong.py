import requests
import re
import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, db='db', user='root', passwd='wxl4174858',
                     charset='utf8')
cursor = db.cursor()


def geImagesList():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
    html = requests.get('https://www.mzitu.com/183109/3',headers=headers).text

    reg = r'src="(.*?)".*?alt="(.*?)"'

    reg = re.compile(reg, re.S)

    imagesList = re.findall(reg, html)
    print(imagesList)

    for i in imagesList:
        images_url = i[0]
        images_title = i[1]
        cursor.execute("insert into images(`name`,`imageurl`) values ('{}','{}')".format(images_title, images_url))
        print('正在保存{}'.format(images_title))
        db.commit()




# for i in (1,10):
geImagesList()
