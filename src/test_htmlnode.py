import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
  def test_assign(self):
    html_node = HTMLNode()
    self.assertEqual(html_node.props, None)  
    self.assertEqual(html_node.value, None)  
    self.assertEqual(html_node.tag, None)  
    self.assertEqual(html_node.children, None)  


if __name__ == "__main__":
  unittest.main()