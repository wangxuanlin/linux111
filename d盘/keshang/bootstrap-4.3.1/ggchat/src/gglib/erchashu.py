# class Ercha:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
# def insert(root, val):
#   if root is None:
#     root=Ercha(val)
#
#   else:
#     if  val<root.val:
#       root.left = insert(root.left,val)
#     elif val>root.val:
#       root.right = insert(root.right,val)
#     return root


class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None


class BTree:
  def __init__(self, dataset):
    self.root = self.creat_node(dataset)

  def creat_node(self, dataset, i=0):
    if i >= len(dataset):
      return
    node = Node()
    node.data = dataset[i]

    left_index = 2 * (i + 1)
    right_index = left_index + 1

    node.left = self.creat_node(dataset, left_index - 1)
    node.right = self.creat_node(dataset, right_index - 1)

    return node

  def _loop(self, node, flag=0):
    if flag < 0:
      yield node.data

    if node.left:
      for d in self._loop(node.left):
        yield d
    if flag == 0:
      yield node.data
    if node.right:
      for d in self._loop(node.right):
        yield d
    if flag > 0:
      yield node.data

  def duilei(self,n,node):
    dataset =[]
    while True:
      dataset[n]= node
      dataset.append(self._loop(node.left))
      dataset.append(self._loop(node.right))



  def __iter__(self):
    return self._loop(self.root)


tree =BTree((1,2,3,4,5,6,7,8,9,10))
for d in tree:
  print(d)
