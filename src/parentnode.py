from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  
  def to_html(self):
    if self.tag == None:
      raise ValueError("missing tag")
    if self.children == None:
      raise ValueError("missing children")
    value = ""
    for c in self.children:
        value += c.to_html()
    return f"<{self.tag}{self.props_to_html()}>{value}</{self.tag}>"
  
  def __repr__(self):
    return '%s(%s, %s, %s, %s)' % (
    self.__class__.__name__, self.tag, self.value,
    self.children, self.props)