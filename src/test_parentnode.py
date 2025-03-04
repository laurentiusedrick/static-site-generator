import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
  def test_assign(self):
    parent_node = ParentNode("p", [])
    self.assertEqual(parent_node.props, None)  
    self.assertEqual(parent_node.value, None)  
    self.assertEqual(parent_node.tag, "p")  
    self.assertEqual(parent_node.children, [])  

  def test_compare(self):
    parent_node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
    self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

  def test_compile(self):
    parent_node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        ParentNode("p", [ 
          LeafNode(None, "Normal text"),
          LeafNode("i", "italic text"),
        ]),
        LeafNode(None, "Normal text")
      ],
)
    self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b><p>Normal text<i>italic text</i></p>Normal text</p>")
  
  def test_compile_empty_children(self):
    parent_node = ParentNode(
      "p",[]
    )
    self.assertEqual(parent_node.to_html(), "<p></p>")


if __name__ == "__main__":
  unittest.main()