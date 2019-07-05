import socket
import os
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addrss = ('127.0.0.1', 8010)
ss.bind(addrss)
ss.listen()
bb = os.path.dirname(__file__)
def cre_gen(res_path):
    h = 'HTTP/1.1 200 OK\r\nDate: Fri, 26 Apr 2019 02:48:05 GMT\r\nServer: nginx\r\nContent-Type: text/html;\r\nConnection: closed\r\n\r\n'
    try:
        with open(os.path.join(bb,'test3(2).html'),'r') as fp:
            mag = fp.read()
        res = (h + mag).encode(encoding='utf8')
    except Exception:
        with open(os.path.join(bb,'表。html'),'r') as fp:
            mag = fp.read()
        res = (h + mag).encode(encoding='utf8')


    return res


while 1:

    cre,add = ss.accept()
    mag = cre.recv(1024)
    mag1 = mag.decode()
    mag1_list = mag1.split('\r\n')
    path = mag1_list[0]
    res_path = path.split(' ')

    res_path1 = res_path[1][1:]
    print(mag1)
    cre.send(cre_gen(res_path1))






