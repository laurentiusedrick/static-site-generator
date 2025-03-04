import unittest

from extractmarkdown import extract_markdown_links, extract_markdown_images

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        self.assertEqual(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"),[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
    
    def test_extract_markdown_links(self):
        self.assertEqual(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"),[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])
    
    def test_extract_markdown_links_false(self):
        self.assertEqual(extract_markdown_links("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"),[])
    
    def test_extract_markdown_images_false(self):
        self.assertEqual(extract_markdown_images("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"),[])

if __name__ == "__main__":
    unittest.main()