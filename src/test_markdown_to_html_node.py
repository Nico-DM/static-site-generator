import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_lists(self):
        md = """
- Item 1 with **bold**
- Item 2 with _italic_

1. First ordered item with `code`
2. Second ordered item with [link](http://example.com)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1 with <b>bold</b></li><li>Item 2 with <i>italic</i></li></ul><ol><li>First ordered item with <code>code</code></li><li>Second ordered item with <a href=\"http://example.com\">link</a></li></ol></div>",
        )

    def test_blockquote(self):
        md = """
>This is a blockquote with **bold** text.
>And _italic_ text here.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote with <b>bold</b> text.\nAnd <i>italic</i> text here.</blockquote></div>",
        )

    def test_mixed_content(self):
        md = """
Here is a paragraph.

```
Code block here
```

>Blockquote here with a [link](http://example.com). `inline code`

- List item 1
- List item 2 with **bold**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Here is a paragraph.</p><pre><code>Code block here</code></pre><blockquote>Blockquote here with a <a href=\"http://example.com\">link</a>. <code>inline code</code></blockquote><ul><li>List item 1</li><li>List item 2 with <b>bold</b></li></ul></div>",
        )

    def test_images_and_links(self):
        md = """
This is an image: ![alt text](http://example.com/image.png) `print("Hello, World!")`
This is a link: [OpenAI](https://openai.com)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is an image: <img src=\"http://example.com/image.png\" alt=\"alt text\"></img> <code>print(\"Hello, World!\")</code> This is a link: <a href=\"https://openai.com\">OpenAI</a></p></div>",
        )


if __name__ == '__main__':
    unittest.main()
