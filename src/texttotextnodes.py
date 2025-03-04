from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter
from splitnodes import split_nodes_image, split_nodes_link


def text_to_textnode(text):
  texts = [TextNode(text, TextType.TEXT)]
  bolded = split_nodes_delimiter(texts, "**", TextType.BOLD)
  italiced = split_nodes_delimiter(bolded, "*", TextType.ITALIC)
  italiced_two = split_nodes_delimiter(italiced, "_", TextType.ITALIC)
  coded = split_nodes_delimiter(italiced_two, "`", TextType.CODE)
  imaged = split_nodes_image(coded)
  linked = split_nodes_link(imaged)
  return linked

