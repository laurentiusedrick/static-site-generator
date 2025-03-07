from enum import Enum

class TextType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"

class TextNode():
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url
  
  def __eq__(self, text_node):
    if not isinstance(text_node, TextNode):
      return False
    return self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url
  
  def __repr__(self):
    return '%s(%s, %s, %s)' % (
    self.__class__.__name__, self.text, self.text_type,
    self.url)