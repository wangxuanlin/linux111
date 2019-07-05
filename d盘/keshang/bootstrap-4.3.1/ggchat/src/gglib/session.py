import json
import threading

from gglib.packet import Packet, PacketRejected

class SessionClosedError(BaseException):
  pass


class Session:
  _session = dict()

  def __init__(self, sock):
    self.sock = sock
    self._packet_queue = []
    self._lock = threading.RLock()
    Session._session[sock.fileno()] = self


  def close(self):
    if self.sock.fileno() in Session._session:
      del Session._session[self.sock.fileno()]
    self.sock.close()


  def recv_packet(self):
    try:
      data = self.sock.recv(65535)
      if not data:
        raise ConnectionError
      json_data = json.load(data.de)


