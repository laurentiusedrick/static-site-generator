import unittest

from block import block_to_block_type, BlockType

class TestBlock(unittest.TestCase):
    def test_block_to_block_type(self):
        par = block_to_block_type("test")

        self.assertEqual(par, BlockType.PARAGRAPH)

        head = block_to_block_type("# Test 123 !@#!@")
        head2 = block_to_block_type("## Test")
        head3 = block_to_block_type("### Test")
        head4 = block_to_block_type("#### Test")
        head5 = block_to_block_type("##### Test")
        head6 = block_to_block_type("###### Test")
        head7 = block_to_block_type("############ Test")
        
        self.assertEqual(head, BlockType.HEADING)
        self.assertEqual(head2, BlockType.HEADING)
        self.assertEqual(head3, BlockType.HEADING)
        self.assertEqual(head4, BlockType.HEADING)
        self.assertEqual(head5, BlockType.HEADING)
        self.assertEqual(head6, BlockType.HEADING)
        self.assertEqual(head7, BlockType.PARAGRAPH)

        code = block_to_block_type("```test ```")
        code2 = block_to_block_type("```test ` ``")
        
        self.assertEqual(code, BlockType.CODE)
        self.assertEqual(code2, BlockType.PARAGRAPH)

        quote = block_to_block_type("> test\n> test2")
        quote2 = block_to_block_type("> test>2>1>")
        
        self.assertEqual(quote, BlockType.QUOTE)
        self.assertEqual(quote2, BlockType.QUOTE)

        ul = block_to_block_type("- test\n* test2\n- test3")
        ul2 = block_to_block_type("- test-test\n- 5*2")
        ul3 = block_to_block_type("*test2\n-test3")
        
        self.assertEqual(ul, BlockType.UL)
        self.assertEqual(ul2, BlockType.UL)
        self.assertEqual(ul3, BlockType.PARAGRAPH)

        ol = block_to_block_type("1. test\n2. test2\n3. test3")
        ol2 = block_to_block_type("1. test-test\n15. 5*2")
        ol3 = block_to_block_type("1.test2\n2.test3")
        
        self.assertEqual(ol, BlockType.OL)
        self.assertEqual(ol2, BlockType.OL)
        self.assertEqual(ol3, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()