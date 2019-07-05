from lei import list
from threading import Condition
import threading

class QueueEmty(BaseException):
  pass


class QueueFull(BaseException):
  pass


class Queue:
  def __init__(self, maxsize):
    self.max_size = maxsize
    self._queue = list()
    self._lock = threading.Lock()
    self._read_cond = Condition(self._lock)
    self._write_cond = Condition(self._lock)


  def _is_full(self):
    return len(self._queue) == self.max_size


  def _is_empty(self):
    return len(self._queue) == 0


  def get(self, block=True):
    self._read_cond.acquire()
    try:
      while self._is_empty():
        Queue._notify(self._write_cond)
        if block:
          self._read_cond.wait()
        else:
          raise QueueEmty
        data = self._queue.pop()
        Queue._notify(self._write_cond)
    finally:
      self._read_cond.release()
    return data
  @staticmethod
  def _notify(cond, time_to_sleep=0.0001):
    cond.notify()
    time.sleep(time_to_sleep)


  def put(self,data, block = False):
    self._write_cond.acquire()
    try:
      while self._is_full():
        Queue._notify(self._read_cond)
      if block:
        self._write_cond.wait()
      else:
        raise QueueFull

      self._queue.append(data)

    finally:
      self._write_cond.release()



if __name__ == '__main__':
  import threadpool
  import threading

  queue = Queue(maxsize=10)
  threads = threadpool.ThreadPool(10)






