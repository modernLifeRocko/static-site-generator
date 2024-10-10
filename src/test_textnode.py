import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def testeq(self):
        node1 = TextNode("This is text", "italic", "https://www.boot.dev/")
        node2 = TextNode("This is text", "italic", "https://www.boot.dev/")
        self.assertEqual(node1, node2)

    def testneq(self):
        node1 = TextNode("This is text og", "italic", "https://www.boot.dev/")
        node2 = TextNode("This is text", "italic", "https://www.boot.dev/")
        self.assertNotEqual(node1, node2)

    def testneqtype(self):
        node1 = TextNode("This is text", "bold", "https://www.boot.dev/")
        node2 = TextNode("This is text", "italic", "https://www.boot.dev/")
        self.assertNotEqual(node1, node2)

    def testnequrl(self):
        node1 = TextNode("This is text", "italic")
        node2 = TextNode("This is text", "italic", "https://www.boot.dev/")
        self.assertNotEqual(node1, node2)



if __name__ == "__main__":
    unittest.main()
