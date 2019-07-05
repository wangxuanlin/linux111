import socket
from select import select


def start_udp_server(address, port):
    pass


def start_tcp_server(address, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((address, port))
    server.listen(10)
    read_list = [server]

    while True:
        fds, _, _ = select(read_list, [], [])
        for fd in fds:
            assert isinstance(fd, socket.socket)
            if fd == server:
                client, addr = fd.accept()
                for r in read_list:
                    if r != server:
                        r.send(("{} is online now".format(addr)).encode("utf-8"))
                read_list.append(client)
                print("{} is online".format(addr))
            else:
                try:
                    data = fd.recv(65535)
                    if not data:
                        raise ConnectionError
                    try:
                        print('{} sent a message:{}'.format(fd.getpeername(), data.decode("utf-8")))
                    except:
                        pass

                    for r in read_list:
                        if r != server and r != fd:
                            r.send(data)
                except ConnectionError:
                    read_list.remove(fd)
                    fd.close()


import argparse
import sys

print(sys.argv)

ap = argparse.ArgumentParser()
ap.add_argument("-t", type=str, choices=("tcp", "udp"), help="to use tcp / udp", default="tcp")
ap.add_argument("-H", type=str, required=True, help="the ip address to bind")
ap.add_argument("-p", type=int, required=True, help="the port to bind")

arg = ap.parse_args(sys.argv[1:])
if arg.t == "tcp":
    start_tcp_server(arg.H, arg.p)
else:
    start_udp_server(arg.H, arg.p)
