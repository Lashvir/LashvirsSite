import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Testing not equal", TextType.ITALIC)
        node2 = TextNode("Testing not equal", TextType.CODE_TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("url node with url set to none", TextType.LINK, None)
        print(f"textnode url with url being none: {node}")

    def test_not_eq2(self):
        node = TextNode("This is testing falseness", TextType.CODE_TEXT)
        node2 = TextNode("This is testing falseness nya", TextType.CODE_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode(
            "This is testing url eq", TextType.IMAGE, "https://www.youtube.com"
        )
        node2 = TextNode(
            "This is testing url eq", TextType.IMAGE, "https://www.youtube.com"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode(
            "This is testing repr self", TextType.LINK, "https://www.youtube.com"
        )
        self.assertEqual(
            "TextNode(This is testing repr self, link, https://www.youtube.com)",
            repr(node),
        )
        print(node)


if __name__ == "__main__":
    unittest.main()
