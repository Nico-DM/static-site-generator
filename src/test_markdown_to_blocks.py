import unittest

from src.markdown_to_blocks import markdown_to_blocks


class MyTestCase(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_markdown(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block(self):
        md = "This is a single block of text without any double newlines."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [md])

    def test_multiple_empty_lines(self):
        md = "First block\n\n\n\nSecond block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block"])

    def test_leading_trailing_newlines(self):
        md = "\n\nLeading and trailing newlines\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Leading and trailing newlines"])

    def test_only_newlines(self):
        md = "\n\n\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


if __name__ == '__main__':
    unittest.main()
