import socket

ss = socket.socket()
addr = ('180.97.33.107',80)
ss.connect(addr)

headers = b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: closed\r\n" \
          b"Cache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: " \
          b"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) " \
          b"Chrome/73.0.3683.86 Safari/537.36\r\nAccept: text/html,application/xhtml+xml," \
          b"application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n\r\n"

ss.send(headers)
print('send ok')
res = b""
while 1:
    msg = ss.recv(65535)
    print('helloword')
    if not msg:
        break
    res += msg

# print(res.decode())
res = res.decode()
res_list = res.split('\r\n\r\n',1)

html = res_list[1]

import os
dir_name = os.path.dirname(__file__)
# jpg_name = dir_name + '/' + '3_1.jpeg'

jpg_name = os.path.join(dir_name,'baidu.html')
with open(jpg_name,'w') as f:
    f.write(html)
