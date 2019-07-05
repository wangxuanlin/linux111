import socket
import threading
conn_lists =[]
def handle_conn(conn, addr):
    while 1:
        msg = conn.recv(1024)
        return_msg = '地址在{}的用户说{}'.format(addr, msg.decod())
        for conn in conn_lists:
            conn.send(return_msg.encode())

def conn_server(addr):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind(addr)
    ss.listen()
    print('服务器已经启动')
    while 1:
        conn,addr = ss.accept()
        conn_lists.append(conn)
        print('链接已经进来了,地址{}'.format(addr))
        handle = threading.Thread(target=handle_conn, args=(conn,))
        handle.start()

if __name__ == '__main__':

    addr =('127.0.0.1', 9521)
    conn_server(addr)

