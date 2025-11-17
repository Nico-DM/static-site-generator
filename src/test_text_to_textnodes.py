import unittest

from src.textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)

    def test_no_formatting(self):
        text = "This is plain text with no formatting."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is plain text with no formatting.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_only_bold(self):
        text = "**Bold Text Only**"
        result = text_to_textnodes(text)
        expected = [
            TextNode("Bold Text Only", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    def test_nested_formatting(self):
        text = "This is **bold and _italic_ text**."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold and _italic_ text", TextType.BOLD),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_nested_formatting_other_way(self):
        text = "This is _italic and **bold** text_."
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_unmatched_delimiter(self):
        text = "This is **bold text with no end."
        with self.assertRaises(ValueError):
            text_to_textnodes(text)


if __name__ == "__main__":
    unittest.main()