
class HTMLNode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    if self.props == None:
      return ""
    result = ""
    for key in self.props:
      result +=f" {key}=\"{self.props[key]}\""
    return result
  
  def __repr__(self):
    return '%s(%s, %s, %s, %s)' % (
    self.__class__.__name__, self.tag, self.value,
    self.children, self.props)
  