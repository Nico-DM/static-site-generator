import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a html node", None, {"class": "text"})
        node2 = HTMLNode("p", "This is a html node", None, {"class": "text"})
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("p", "This is a html node", None, {"class": "text"})
        node2 = HTMLNode("p", "This is a different html node", None, {"class": "text"})
        self.assertNotEqual(node, node2)

        node3 = HTMLNode("div", "This is a html node", None, {"class": "text"})
        self.assertNotEqual(node, node3)

    def test_repr(self):
        node = HTMLNode(None, "Sample text", None, None)
        expected_repr = "HTMLNode(None, Sample text, [], {})"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()