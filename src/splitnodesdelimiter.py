from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  result = []

  for node in old_nodes:
    if not isinstance(node, TextNode):
      raise ValueError("Not a TextNode")
    if node.text_type != TextType.TEXT:
      result.append(node)
      continue
    if node.text.count(delimiter) % 2 != 0:
      raise Exception("Invalid Markdown syntax")
    new_nodes = []
    texts = node.text.split(delimiter)
    for i, t in enumerate(texts):
      if i % 2 == 0:
        new_nodes.append(TextNode(t, TextType.TEXT))
      else:
        new_nodes.append(TextNode(t, text_type))
    
    result.extend(new_nodes)
  return result
