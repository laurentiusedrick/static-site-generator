import unittest

from textnode import TextNode, TextType
from textnodetothmlnode import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text = TextNode("This is a text node", TextType.TEXT)
        bold = TextNode("This is a text node", TextType.BOLD)
        italic = TextNode("This is a text node", TextType.ITALIC)
        code = TextNode("This is a text node", TextType.CODE)
        link = TextNode("This is a text node", TextType.LINK, "https://link.com")
        image = TextNode("This is a text node", TextType.IMAGE, "https://image.com")

        self.assertEqual(text_node_to_html_node(text).to_html(), "This is a text node")
        self.assertEqual(text_node_to_html_node(bold).to_html(), "<b>This is a text node</b>")
        self.assertEqual(text_node_to_html_node(italic).to_html(), "<i>This is a text node</i>")
        self.assertEqual(text_node_to_html_node(code).to_html(), "<code>This is a text node</code>")
        self.assertEqual(text_node_to_html_node(link).to_html(), "<a href=\"https://link.com\">This is a text node</a>")
        self.assertEqual(text_node_to_html_node(image).to_html(), "<img src=\"https://image.com\" alt=\"This is a text node\"></img>")

if __name__ == "__main__":
    unittest.main()