import unittest

from block_to_blocktype import block_to_blocktype, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        text = "This is a simple paragraph."
        self.assertEqual(block_to_blocktype(text), BlockType.PARAGRAPH)

    def test_heading(self):
        text = "## This is a heading"
        self.assertEqual(block_to_blocktype(text), BlockType.HEADING)

    def test_code(self):
        text = "```\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_blocktype(text), BlockType.CODE)

    def test_quote(self):
        text = ">This is a quote.\n>It has multiple lines."
        self.assertEqual(block_to_blocktype(text), BlockType.QUOTE)

    def test_unordered_list(self):
        text = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_blocktype(text), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        text = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_blocktype(text), BlockType.ORDERED_LIST)


if __name__ == '__main__':
    unittest.main()
