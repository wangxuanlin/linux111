import socket
import os
#new出来一个socket对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
server.bind(('0.0.0.0',8001))

server.listen()
base_dir = os.path.dirname(__file__)
def msg_gen():
    headers = "HTTP/1.1 200 OK\r\nDate: Fri, 26 Apr 2019 02:48:05 GMT\r\nServer: nginx\r\nContent-Type: text/html;\r\nConnection: closed\r\n\r\n"
    with open(os.path.join(base_dir,'test3.html'),'r') as fp:
        msg = fp.read()
    print('-------------')
    print(msg)
    print('-------------')
    res_msg = (headers+msg).encode(encoding='utf8')

    return res_msg



while True:
    conn,addr = server.accept()
    msg = conn.recv(65535)
    print(msg)
    conn.send(msg_gen())

