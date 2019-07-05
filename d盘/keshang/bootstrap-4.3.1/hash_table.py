from sys import getrefcount
from lei import list


class Hashtable:
  def __init__(self,size):
    links =list()
    self.size = size
    for i in range(size):
      links.append(list( ))
    self.links = tuple(links)


  def _get_hash_id_by_key(self,key):
    assert isinstance(key,bytes)
    sum = 0
    for k in key:
      sum += k
    return sum % self.size


  def put(self,key, value):
    hash_id = self._get_hash_id_by_key(key, encode('utf-8'))



