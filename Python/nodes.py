class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Creating the nodes
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# Yacko keeps track of dots info
yacko.set_link_node(dot)
# Dot keeps track of wackos info
dot.set_link_node(wacko)
# Poor wacko doesn't keep track of anybody's data

# To access dots info, we get the link from yacko and get the value from the node yacko's pointing to
dots_data = yacko.get_link_node().get_value()
# Same thing for wackos data, use dot
wackos_data = dot.get_link_node().get_value()
print(dots_data)
print(wackos_data)
