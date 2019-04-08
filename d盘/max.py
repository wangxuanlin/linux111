# import socket
# import threading
#
# ss = socket.socket()
# ss.connect(('127.0.0.1', 9519))
#
#
# def conn_send(ss):
#     while 1:
#         msg = input('输入消息')
#         try:
#           ss.send(msg.encode())
#         except Exception:
#             break
#     print('发送程序已经结束')
#
#
# def conn_recv(ss):
#     while 1:
#         return_msg = ss.recv(1024)
#         if not return_msg:
#             break
#         print(return_msg.decode())
#
# t1 = threading.Thread(target=conn_send,args=(ss,))
# t2 = threading.Thread(target=conn_recv, args=(ss,))
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# coding: utf8
c





