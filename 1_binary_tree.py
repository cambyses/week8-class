# Let's build a data structure using a binary tree.
class BTreeNode:

  def __init__(self):
    self.data = None
    self.left = None
    self.right = None


class BTree:

  def __init__(self):
    self.root = None

  def __str__(self):
    if self.root != None:
      return "BTree nodes: " + str(self.root.data)
    else:
      return "(no nodes yet)"

  def find(data):
    pass

  def add(self, data, node = None):
    if self.root == None:
      self.root = BTreeNode()
      self.root.data = data
      return

    if node == None:
      node = self.root

    if data < node.data:
      if node.left == None:
        node.left = BTreeNode()
        node.left.data = data
      else:
        self.add(data, node.left)
    else:
      if node.right == None:
        node.right = BTreeNode()
        node.right.data = data
      else:
        self.add(data, node.right)







  def display(self, node = None):
    if node == None:
      node = self.root

    if node.left != None:
      self.display(node.left)

    print(node.data)

    if node.right != None:
      self.display(node.right)



tree = BTree()
tree.add(21)
tree.add(3)
tree.add(16)
tree.add(0)
tree.add(42)
tree.add(17)
tree.add(5)

tree.display()





