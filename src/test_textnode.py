import unittest
from htmlnode import LeafNode
from textnode import TextNode, text_node_to_html_node


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


class NodeConvertTest(unittest.TestCase):
    def testtxtconvert(self):
        txt = TextNode('random text', 'text')
        htmltxt = text_node_to_html_node(txt)
        goalhtml = LeafNode(None, 'random text')
        self.assertEqual(htmltxt, goalhtml)

    def testimgconvert(self):
        txtnode = TextNode('image description', 'image', '/img/dir')
        htmlimg = text_node_to_html_node(txtnode)
        goalhtml = LeafNode('img', '',
                            {'src': '/img/dir', 'alt': 'image description'})
        self.assertEqual(htmlimg, goalhtml)

    def testlinkconvert(self):
        txtnode = TextNode('text link', 'link', '/link/dir')
        htmla = text_node_to_html_node(txtnode)
        goalhtml = LeafNode('a', 'text link', {'href': '/link/dir'})
        self.assertEqual(htmla, goalhtml)

    def testfalsetxttype(self):
        txtnode = TextNode('sample text', 'ling')
        self.assertRaises(ValueError, lambda: text_node_to_html_node(txtnode))


if __name__ == "__main__":
    unittest.main()
