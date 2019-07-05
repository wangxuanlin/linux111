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
import select, socket

response = b"hello world"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('127.0.0.1', 8080))
serversocket.listen(1)
serversocket.setblocking(0)

poll = select.poll()
poll.register(serversocket.fileno(), select.POLLIN)

connections = {}
while True:
    for fd, event in poll.poll():
        if event == select.POLLIN:
            if fd == serversocket.fileno():
                con, addr = serversocket.accept()
                poll.register(con.fileno(), select.POLLIN)
                connections[con.fileno()] = con
            else:
                con = connections[fd]
                data = con.recv(1024)
                if data:
                    poll.modify(con.fileno(), select.POLLOUT)
        elif event == select.POLLOUT:
            con = connections[fd]
            con.send(response)
            poll.unregister(con.fileno())
            con.close()






