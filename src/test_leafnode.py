import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
  def test_assign(self):
    leaf_node = LeafNode()
    self.assertEqual(leaf_node.props, None)  
    self.assertEqual(leaf_node.value, None)  
    self.assertEqual(leaf_node.tag, None)  
    self.assertEqual(leaf_node.children, None)  

  def test_compare(self):
    leaf_node = LeafNode("p", "test", {"font": "bold"})
    self.assertEqual(leaf_node.to_html(), "<p font=\"bold\">test</p>")


if __name__ == "__main__":
  unittest.main()