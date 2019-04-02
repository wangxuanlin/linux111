# import socket
# import os
#
# sk = socket.socket()
#
# print(sk)
#
# address = ('127.0.0.1', 8000)
# sk.bind(address)
# sk.listen(3)
# print('waiting.......')
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# while 1:
#     conn,addr = sk.accept()
#     while 1:
#         filename = '123456789.jpg'
#         path = os.path.join(BASE_DIR, 'MNIST_80', filename)
#         f = open(path, 'ab')
#         has_receive = 0
#
#         data =conn.recv(1024)
#         f.write(data)
#         f.close()
#         print(data)
#
# import socket
# import os
#
# sk = socket.socket()
# print(sk)
#
# address = ('127.0.0.1', 8000)
# sk.connect(address)
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#
# while True:
#     inp = input('>>>>>>>>')
#
#     cmd, path = inp.split('|')
#
#     path = os.path.join(BASE_DIR, path)
#
#     filename = os.path.basename(path)
#
#     file_size = os.stat(path).st_size
#
#     file_info = 'post|%s|%s' % (filename, file_size)
#     sk.sendall(bytes(file_info, 'utf8'))
#
#     f = open(path, 'rb')
#     has_sent = 0
#     while has_sent != file_size:
#         data = f.read(1024)
#         sk.sendall(data)
#         has_sent += len(data)
#
#     f.close()
#     print('上传成功')
import socket
import sys
import time

if __name__ == '__main__':
    # 创建套接字
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.eorror, e:
        print
        'socket false:%s' % e
    print
    'socket ...'

    # 连接百度ip
    try:
        sock.connect(('220.181.111.148', 80))
    except socket.error, e:
        print
        'connect false %s' % e
        sock.close()
    print
    'connect ...'

    # 发送百度首页面请求并且保持连接
    try:
        print
        'send start...'
        str = 'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:keep-alive\r\n\r\n'
        sock.send(str)
    except socket.eorror, e:
        print('send false')
        sock.close()

    data = ''
    data = sock.recv(1024)
    while (1):
    print(data)
    beg = data.find('Content-Length:', 0, len(data))
    end = data.find('Content-Type:', 0, len(data))
    print(beg)
    print(end)
    if (beg == end):
        print('connecting closed')
        break
    num = long(data[beg + 16:end - 2])
    print(num)
    nums = 0
    while (1):
        data = sock.recv(1024)
        print(data)
        nums += len(data)
        if (nums >= num):
            break
    word = raw_input('please input your word----->')
    str = '''GET /s?wd=''' + word + ''' HTTP/1.1
Host:www.baidu.com
Connection: Keep-Alive
'''
    print(str)
    sock.send(str)
    data = ''
    data = sock.recv(1024)
sock.close()
print(data)

---------------------
