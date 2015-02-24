class Node:

  def __init__(self):
    self.data = None
    self.next = None


class GroceryList:

  def __init__(self):
    self.root = None

  # This version would insert new items
  # at the head of the list.
  #
  # def add(self, name_of_food):
  #   new_node = Node()
  #   new_node.data = name_of_food

  #   if self.root is None:
  #     self.root = new_node
  #   else:
  #     new_node.next = self.root
  #     self.root = new_node

  # This version adds new items to
  # the end of the list.
  def add(self, name_of_food):
    new_node = Node()
    new_node.data = name_of_food

    if self.root is None:
      self.root = new_node
    else:
      current_node = self.root
      while current_node.next != None:
        current_node = current_node.next

      current_node.next = new_node

  def at():
    pass

  def display(self, node):
    if node != None:
      print(node.data)
      self.display(node.next)

  # def display(self):
  #   current_node = self.root
  #   while current_node is not None:
  #     print(current_node.data)
  #     current_node = current_node.next

  def display_reverse():
    pass

  def sort():
    pass

groceries = GroceryList()
groceries.add("cookies")
groceries.add("ice cream")
groceries.add("pizza")
groceries.display(groceries.root)

# print(groceries.at(1))  # => "ice cream"

# groceries2 = GroceryList()
# groceries2.add("broccoli")
# groceries2.add("apples")





