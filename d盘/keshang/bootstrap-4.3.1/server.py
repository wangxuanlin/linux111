import socket
from select import select, poll, POLLIN, POLLOUT


def start_udp_server(address, port):
  udp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  udp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
  udp_server.bind((address, port))
  clients = []
  while True:
    data, addr = udp_server.recvfrom(65535)
    if addr not in clients:
      clients.append(addr)
    for c in clients:
      udp_server.sendto(data, c)
  udp_server.close()


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
    ready_fds = p.poll()
    for fd, ev in ready_fds:
      if ev & POLLIN:
        if fd == server.fileno():
          client, addr = server.accept()
          clients[client.fileno()] = client
          for c in clients.keys():
            p.register(c, POLLOUT | POLLIN)
        else:
          client = clients[fd]
          try:
            data = client.recv(65535)
            if not data:
              raise ConnectionError
            try:
              print("{} sent a message:{}".format(server.getpeername(), data.decode("utf-8")))
            except:
              pass
          except ConnectionError:
            client.close()
            p.unregister(fd, POLLIN)
      if ev & POLLOUT:
        if fd == server.fileno():
          pass





def start_tcp_server_with_select(address, port):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((address, port))
  server.listen(10)
  read_list = [server]
  write_list = []

  while True:
    read_fds, write_fds, _ = select(read_list, write_list, [])
    for fd in read_fds:
      assert isinstance(fd, socket.socket)
      if fd == server:
        client, addr = fd.accept()
        for r in read_list:
          if r != server:
            if r not in send_queue:
              send_queue[r] = []
            data_queue = send_queue[r]
            data_queue.append(("{} is online now".format(addr)).encode("utf-8"))
            data_queue.append(("{} is online now(2)".format(addr)).encode("utf-8"))
            if r not in write_list:
              write_list.append(r)

        read_list.append(client)
        print("{} is online".format(addr))
      else:
        try:
          data = fd.recv(65535)
          if not data:
            raise ConnectionError
          try:
            print("{} sent a message:{}".format(fd.getpeername(), data.decode("utf-8")))
          except:
            pass
          for r in read_list:
            if r != server and r != fd:
              if r not in send_queue:
                send_queue[r] = []
              data_queue = send_queue[r]
              data_queue.append(data)
              if r not in write_list:
                write_list.append(r)
        except ConnectionError:
          read_list.remove(fd)
          fd.close()

      for fd in write_fds:
        if fd not in send_queue:
          write_list.remove(fd)
          continue

        data_queue = send_queue[fd]
        data = data_queue.pop(0)
        fd.send(data)
        if not data_queue:
          del send_queue[fd]
          write_list.remove(fd)



# import argparse
# import sys
#
# print(sys.argv)
# ap = argparse.ArgumentParser()
# ap.add_argument("-t", type =str, choices=("tcp","udp"),help="to use tcp/udp",default="tcp")
# ap.add_argument("-H", type =str, required=True,help="the ip address to bind")
# ap.add_argument("-t", type =str, required=True,help="the port to bine")

start_tcp_server_with_select("127.0.0.1", 8899)
