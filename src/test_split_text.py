import unittest

from src.split_text import split_nodes_delimiter, split_nodes_image, split_nodes_link
from src.textnode import TextNode, TextType


class TestSplitText(unittest.TestCase):
    def test_split_bold(self):
        nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_italic(self):
        nodes = [TextNode("This is *italic* text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        nodes = [TextNode("This is **bold text", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_non_text_node(self):
        nodes = [TextNode("This is a link", TextType.LINK, "https://example.com")]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is a link", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(result, expected)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example.org)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://example.org"),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):
        node = TextNode(
            "This is text without any links.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text without any links.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode(
            "This is text without any images.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text without any images.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_mixed_content(self):
        node = TextNode(
            "Here is **bold text**, an ![image](https://i.imgur.com/zjjcJKZ.png), and a [link](https://example.com).",
            TextType.TEXT,
        )
        nodes_after_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
        nodes_after_image = split_nodes_image(nodes_after_bold)
        final_nodes = split_nodes_link(nodes_after_image)
        self.assertListEqual(
            [
                TextNode("Here is ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(", an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(", and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(".", TextType.TEXT),
            ],
            final_nodes,
        )


if __name__ == '__main__':
    unittest.main()
