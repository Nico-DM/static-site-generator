import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


class TestSplitText(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_links_no_image(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_images_no_link(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_no_matches(self):
        matches_images = extract_markdown_images(
            "This is text with no images or links."
        )
        matches_links = extract_markdown_links(
            "This is text with no images or links."
        )
        self.assertListEqual([], matches_images)
        self.assertListEqual([], matches_links)

    def test_multiple_matches(self):
        matches_images = extract_markdown_images(
            "![img1](url1) some text ![img2](url2)"
        )
        matches_links = extract_markdown_links(
            "[link1](url1) some text [link2](url2)"
        )
        self.assertListEqual([("img1", "url1"), ("img2", "url2")], matches_images)
        self.assertListEqual([("link1", "url1"), ("link2", "url2")], matches_links)

    def test_empty_alt_text_and_url(self):
        matches_images = extract_markdown_images(
            "![](url) ![alt]()"
        )
        matches_links = extract_markdown_links(
            "[](url) [alt]()"
        )
        self.assertListEqual([("", "url"), ("alt", "")], matches_images)
        self.assertListEqual([("", "url"), ("alt", "")], matches_links)


if __name__ == '__main__':
    unittest.main()
