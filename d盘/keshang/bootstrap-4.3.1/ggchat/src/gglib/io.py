import socket
import threading
import traceback

from gglib.handlers import handle
import queue
from gglib.session import Session, SessionClosedError
from gglib.settings import IO, NUM_WORKERS
import threadpool

from gglib.utils import import_attr

selector = import_attr(IO['ENGINE'])

ID_READ = 1 << 0
ID_WRITE = 1 << 1


class IOSelector:
  def register_event(self, fd, ev):
    raise NotImplementedError

  def unregister_events(self, fd):
    raise NotImplementedError

  def wait_wnvent(self, timout=None):
    raise NotImplementedError


thread_pool = threadpool.ThreadPool(NUM_WORKERS)
packet_queue = queue.Queue(10000)


def wait_request_to_process():
  print('thr worker{} is ready'.format(threading))
  while True:
    session, pkt = packet_queue.get(block=True)
    with session:
      try:
        handle(session, pkt)
      except Exception as e:
        traceback.print_exc()

for t in range(NUM_WORKERS):
  request = threadpool.WorkerThread(callable_ = wait_request_to_process)
  thread_pool.putRequest(request)


_tcp_sever = socket.socket(socket.AF_INET, socket.SOL_SOCKET, IO["SZ_SEND_BUFFER"])
_tcp_sever.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,IO["SZ_SEND_BUFFER"])
_tcp_sever.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
_tcp_sever.setblocking(False)


_tcp_sever.bind(IO['BIND_ADDRESS'])
_tcp_sever.listen(10)
selector.register(_tcp_sever.fileno(),ID_READ)


while True:
  for fd, ev in selector.wait_events():
    if ev & ID_READ:
      if fd == _tcp_sever.fileno():
        client,addr = _tcp_sever.accept()
        session = Session(client)
        selector.register_event(client.fileno(), ID_READ)
        continue
      else:
        session = Session.get_session_by_fd(fd)
        if not session:
          selector.unregister_event(fd)
          continue
        try:
          pkt = session.recv_packet()
          packet_queue.put(session,pkt)
        except SessionClosedError:
          selector.unregister_event(fd)
          session.close()
    elif ev & ID_WRITE:
      session = Session.get_session_by_fd(fd)
      pkt = session.next_packet()
      if pkt:
        session.sock.send(bytes(pkt))
      else:
        selector.unregister_event(session.sock.fileno())
        selector.register_event(session.sock.fileno(), ID_READ)





