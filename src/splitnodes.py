from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
  result = []

  for node in old_nodes:
    if not isinstance(node, TextNode):
      raise ValueError("Not a TextNode")
    image_attrs = extract_markdown_images(node.text)
    if len(image_attrs) == 0 or node.text_type != TextType.TEXT:
      result.append(node)
      continue

    text = node.text
    for img_attr in image_attrs:
      texts = text.split(f"![{img_attr[0]}]({img_attr[1]})", 1)
      new_nodes = []

      if texts[0] != "":
        new_nodes.append(TextNode(texts[0], TextType.TEXT))

      new_nodes.append(TextNode(img_attr[0], TextType.IMAGE, img_attr[1]))

      if len(extract_markdown_images(texts[1])) != 0:
        result.extend(new_nodes)
        text = texts[1]
        continue

      if texts[1] != "":
        new_nodes.append(TextNode(texts[1], TextType.TEXT))
      result.extend(new_nodes)
    
  return result

def split_nodes_link(old_nodes):

  result = []

  for node in old_nodes:
    if not isinstance(node, TextNode):
      raise ValueError("Not a TextNode")
    links_attrs = extract_markdown_links(node.text)
    if len(links_attrs) == 0 or node.text_type != TextType.TEXT:
      result.append(node)
      continue

    text = node.text
    for link_attr in links_attrs:
      texts = text.split(f"[{link_attr[0]}]({link_attr[1]})", 1)
      new_nodes = []

      if texts[0] != "":
        new_nodes.append(TextNode(texts[0], TextType.TEXT))

      new_nodes.append(TextNode(link_attr[0], TextType.LINK, link_attr[1]))

      if len(extract_markdown_links(texts[1])) != 0:
        result.extend(new_nodes)
        text = texts[1]
        continue

      if texts[1] != "":
        new_nodes.append(TextNode(texts[1], TextType.TEXT))
      result.extend(new_nodes)
    
  return result

