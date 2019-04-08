# import socket
# import threading
# conn_lists =[]
# def handle_conn(conn, addr):
#     while 1:
#         msg = conn.recv(1024)
#         return_msg = '地址在{}的用户说{}'.format(addr, msg.decode())
#         for conn in conn_lists:
#             conn.send(return_msg.encode())
#
# def conn_server(addr):
#     ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     ss.bind(addr)
#     ss.listen()
#     print('服务器已经启动')
#     while 1:
#         conn, addr = ss.accept()
#         conn_lists.append(conn)
#         print('链接已经进来了,地址{}'.format(addr))
#         handle = threading.Thread(target=handle_conn, args=(conn, addr))
#         handle.start()
#
# if __name__ == '__main__':
#
#     addr = ('127.0.0.1', 9519)
#     conn_server(addr)

import socket
import subprocess
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
add = ('127.0.0.1', 16183)
server.bind(add)
server.listen(5)

while 1:
    print('waiting....')
    conn, addr = server.accept()
    print('-->conn:', conn)
    print('--addr:',addr)
    print('got it....')


    while 1:
        try:
            cmd = conn.recv(1024)
            res = subprocess.Popen(cmd.decode('utf-8'), shell= True,
                                   stdout= subprocess.PIPE,
                                   stderr= subprocess.PIPE)

            conn.send(res.stdout.read())
            conn.send(res.stderr.read())
        except Exception:
            break
    conn.close()



