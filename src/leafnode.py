from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    super().__init__(tag, value, None, props)

  
  def to_html(self):
    if self.value == None:
      raise ValueError("missing value")
    if self.tag == None:
      return self.value
    
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
  
  def __repr__(self):
    return '%s(%s, %s, %s, %s)' % (
    self.__class__.__name__, self.tag, self.value,
    self.children, self.props)