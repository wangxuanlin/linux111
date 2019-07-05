import socket
from select import select, poll, POLLIN, POLLOUT
send_queue = {}

def start_tcp_server_with_poll(address, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((address, port))
    server.listen(10)
    clients = {}
    p = poll()
    p.register(server.fileno(), POLLIN)
    while True:
        read_fds = p.poll()
        for fd, ev in read_fds:
            if ev & POLLIN:
                if fd == server.fileno():
                    client, addr = server.accept()
                    clients[client.fileno()] = client
                    for c in clients.keys():
                        if c not in send_queue:
                            send_queue[c] = []
                            data_queue = send_queue[c]
                            data_queue.append(('{} is on line'.format(addr)).encode('utf-8'))
                        p.register(c, POLLIN | POLLOUT)
                        print('{} is online'.format(addr))
                else:
                    client = clients[fd]
                    try:
                        data = client.recv(65535)
                        if not data:
                            raise ConnectionError
                        try:
                            print('{}send a message:{}'.format(client.getpeername(), data.decode('utf-8')))
                        except:
                            pass
                        for k in clients.keys():
                            if k != server.fileno() and k != fd:
                                if k not in send_queue:
                                    send_queue[k] = []
                                data_queue = send_queue[k]
                                data_queue.append(data)
                                p.register(k, POLLOUT|POLLIN)
                    except ConnectionError:
                        client.close()
                        p.unregister(fd)
            if ev & POLLOUT:
                if fd not in send_queue:
                    p.register(fd, POLLIN)
                    continue
                data_queue = send_queue[fd]
                data = data_queue.pop(0)
                client = clients[fd]
                client.send(data)
                if not data_queue:
                    del send_queue[fd]
                    p.register(fd, POLLIN)