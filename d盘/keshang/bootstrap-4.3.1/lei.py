class Node:
  def __init__(self):
    self.data = None
    self.next = None
    self.prev = None


class Link:

  def __init__(self, data=()):
    self.head = Node()  # 实利化头节点
    self.tail = self.head  # 指针指向开头
    self.length = 0
    for d in data:
      self.append(d)

  def __find__node_by(self, pos):
    nodeptr = self.head
    while pos:
      nodeptr = nodeptr.next
      pos -= 1
    return nodeptr

  def append(self, data):
    node = Node()
    node.data = data
    self.tail.next = node
    node.prev = self.tail
    self.tail = node
    self.length += 1

  def pop(self, i=-1):
    if len(self) <= 0:
      raise Exception('THE LIST IS EMPTY')
    if i == -1:
      node = self.tail
      self.tail.next = None
      self.length -= 1
      return node.data
    else:
      node = self.__find__node_by(i)
      cur_node = node.next
      third_node = node.next.next
      if third_node is not None:
        third_node.prev = node
      node.next = third_node
      self.length -= 1
      return cur_node.data

  def insert(self, i, data):

    assert i <= len(self) - 1
    nodeptr = self.head
    while i:
      nodeptr = nodeptr.next
      i -= 1
    third_node = nodeptr.next
    node = Node()
    third_node.prev = nodeptr
    node.prev = node
    self.length += 1

  def remove(self, i):
    assert i <= len(self) - 1
    nodeptr = self.__find__node_by(i)
    third_node = nodeptr.next.next
    nodeptr.next = third_node
    third_node.prev = nodeptr
    self.length -= 1

  def __len__(self):
    return self.length

  def __iter__(self):
    return LinkIterator(self)

  def __setitem__(self, key, value):
    assert key <= len(self) - 1
    nodeptr = self.__find__node_by(key)
    nodeptr.next.data = value
    return nodeptr

  def __add__(self, other):
    for i in other:
      self.append(i)
    return self

  def __iadd__(self, other):
    for i in self:
      i = i + other
      self.append(i)
      return self

  def __sub__(self, other):
    pass

  def __isub__(self, other):
    pass

  def __mul__(self, other):
    pass

  def __divmod__(self, other):
    pass


  def __contains__(self, item):
    for d in self:
      if d == item:
        return True
    return False
def recerse(link, m):
  def recursive(node, m):
    first_node = node.next
    if first_node == None:
        return
    n = m -1
    while n:
      nn = first_node.next
      if not nn:
        return
      # 移除当前节点'nn'
      first_node.next = nn.next
      if nn.next:
        nn.next.prev = first_node
      # 将当前节点插入到第一个位置
      nn.next = node.next
      node.next = nn
      nn.prev = node
      n -= 1
    recursive(first_node, m)
  recursive(link.head, m)





class LinkIterator:
  def __init__(self, link):
    self._node_ptr = link.head

  def __next__(self):
    self._node_ptr = self._node_ptr.next
    if self._node_ptr is None:
      raise StopIteration
    data = self._node_ptr.data
    return data


list = Link
x = list()
x.append(1)
x.append(2)
x.append(3)
x.append(4)

x.__iadd__(2)
for i in x:
  print(i)

# print(x.__setitem__(1, 8))
# for i in x:
#   print(i)
#
# print(x.pop(2))
# for i in x:
#   print(i)

