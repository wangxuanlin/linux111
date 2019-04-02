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
# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.baidu.com', 80))
# s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection: close\r\n\r\n')
#
# buffer = []
# while 1:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
#
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# with open('baidu.html', 'wb')as f:
#     f.write(html)
# import os
# dir_name = os.path.dirname(__file__)
#
# jpg_name = os.path.join(dir_name, '3_1.png')
# jpg_name1 = os.path.join(dir_name, '3_1_copy1.png')
#
# with open(jpg_name, 'rb') as f:
#     b_file = f.read()
#
# with open(jpg_name, 'wb') as f:
#     f.write(b_file)


import socket

addrss = ('127.0.0.1', 1310)
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(addrss)
ss.listen(1)
print('Sering HTTP on port %s ...'%1310)
while 1:
    cli, add = ss.accept()
    request = cli.recv(1024)
    print(request)
    http_response = b'''
    HTTP/1.1 200 OK\r\n\r\n
    HELLO,WORLD'''
    cli.send(http_response)
    cli.close()