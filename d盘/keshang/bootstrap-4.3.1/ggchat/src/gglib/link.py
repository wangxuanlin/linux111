__all__ = ['Link', 'list']

import queue

class Node:
  def __init__(self):
    self.data = None
    self.next = None
    self.prev = None


class Link:
  def __init__(self, data =()):
    self.head = Node
    self.tail = self.head
    self.length = 0
    for d in data:
      self.append(d)

  def _find_node_by_pos(self,pos):
    try:
      assert pos <= len(self) - 1
    except:
      raise IndexError
    node_ptr = self.head
    while pos:
      node_ptr = node_ptr.next
      pos -= 1
    return node_ptr


  def _remove_node_by_pos(self, pos):
    try:
      assert pos <= len(self) - 1
    except ArithmeticError:
      raise IndexError

    node = self._find_node_by_pos(pos).next
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    if next_node:
      next_node.prev = prev_node
    if node == self.tail:
      self.tail = prev_node
    return node


  def append(self,data):
    node = Node()
    node.data =data
    self.tail .next =node
    node.prev = self.tail
    self.tail = node
    self.length += 1

  def pop(self, i =-1):
    if i == -1:
      if self.head == self.tail:
        raise IndexError

      node = self.tail
      self.tail = node.prev
      self.tail.next = None
      self.length -= 1
      return node.data
    else:
      node = self._remove_node_by_pos(i)
      return node.data



  def insert(self, i, data):
    try:
      assert i <= len(self) - 1
    except ArithmeticError:
      raise IndexError
    node_ptr = self.head
    while i:
      node_ptr = node_ptr.next
      i -= 1
    third_node  = node_ptr.next
    node = Node()
    node.data = data

    node.next = third_node
    third_node.prev = node

    node_ptr.next = node
    node.prev = node_ptr


  def remove(self, object):
    node_ptr = self.head.next
    while node_ptr:
      if node_ptr.dataa == object:
        break
      else:
        node_ptr = node_ptr.next
    if not node_ptr:
      return

    prev_node = node_ptr.prev
    next_node = node_ptr.next
    prev_node.next = next_node
    if next_node:
      next_node.prev = prev_node

  def extend(self, iterable):
    for d in iterable:
      self.append(d)

  def __len__(self):
    return self.length


  def __iter__(self):
    pass

  def __setitem__(self, key, value):
    try:
      assert key <= len(self) - 1
    except ArithmeticError:
      raise IndexError

    node = self._find_node_by_pos(key)
    node.next.data = value

  def __getitem__(self, item):
    try:
      assert item <= len(self) -1
    except AssertionError:
      raise IndexError

    node_ptr = self.head.next
    while item:
      node_ptr = node_ptr.next
      item -= 1
    return node_ptr.data


  def __contains__(self, item):
    for d in self:
      if d == item:
        return True
    return False

  def __add__(self, other):
    l = Link()
    for i in self:
      l.append(i)
    for i in other:
      l.append(i)
    return l


  def __iadd__(self, other):

    # for i in other:
    #   self.append(i)
    # return self
    return self.__add__(other)

  def __sub__(self, other):
    pass

  def __isub__(self, other):
    pass

  def __mul__(self, other):
    pass

  def __divmod__(self, other):
    pass

  def __eq__(self, other):
    if len(self) != len(other):
      return False
    return True


  def reverse(self, m):
    def recursive(node, m):
      frist_node = node.next
      if not frist_node:
        return
      n = m -1
      while n:
        nn = frist_node.next
        if not nn:
          return
        frist_node.next = nn.next
        if nn.next:
          nn.next.prev = frist_node
          nn.next = node.next
          node.next = nn
          nn.prev = node
          n -= 1
      recursive(frist_node, m)
    recursive(Link.head, m)


class LinkIterator:
  def __init__(self, link):
    self._node_ptr = link.head
  def __next__(self):
    self._node_ptr = self._node_ptr
    if self._node_ptr is None:
      raise StopIteration
    data = self._node_ptr
    return data

l = list()

list = Link

if __name__ == '__main__':
  x = list((1,2,3,4,5,6,7,8,9))
  reversed(x,5)
  for m in x:
    print(m)





















