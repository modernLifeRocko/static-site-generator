import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class HTMLNodeTest(unittest.TestCase):
    def testpropsnochild(self):
        node = HTMLNode('p', 'this is a paragraph', None,
                        {'color': 'black', 'margin': 'auto'})
        # print(node)
        propsstr = node.props_to_html()
        self.assertEqual(propsstr, ' color=black margin=auto')

    def testnopropschild(self):
        node1 = HTMLNode('li', 'first list item')
        node2 = HTMLNode('li', 'second list item')

        listnode = HTMLNode('ol', None, [node1, node2])
        # print(listnode)

        propstr = listnode.props_to_html()
        self.assertEqual(propstr, '')

    def testchildprop(self):
        node1 = HTMLNode('p', 'this is text')
        pnode = HTMLNode('div', None, [node1], {'margin': 'auto'})

        pstr = pnode.props_to_html()
        self.assertEqual(pstr, ' margin=auto')


class LeafNodeTest(unittest.TestCase):
    def testNoValue(self):
        node = LeafNode('p', None)
        self.assertRaises(ValueError, node.to_html)

    def testNoTag(self):
        node = LeafNode(None, 'this is just text')
        self.assertEqual('this is just text', node.to_html())

    def testNoProps(self):
        node = LeafNode('p', 'text')
        html_str = '<p>text</p>'
        self.assertEqual(html_str, node.to_html())

    def testWithProps(self):
        node = LeafNode('div', '', {'margin': 'auto',
                                    'background-color': 'blue'})
        node_str = '<div margin=auto background-color=blue></div>'
        self.assertEqual(node_str, node.to_html())


class ParentNodeTest(unittest.TestCase):
    def testnotag(self):
        node = ParentNode(None, [])
        self.assertRaises(ValueError, node.to_html)

    def testnochild(self):
        node = ParentNode('ol', None)
        self.assertRaises(ValueError, node.to_html)

    def testlistTest(self):
        item1 = LeafNode('li', 'First item')
        item2 = LeafNode('li', 'Second item')
        lnode = ParentNode('ol', [item1, item2])
        lst_str = "<ol>\n<li>First item</li>\n<li>Second item</li>\n</ol>"
        node_str = lnode.to_html()
        # print(lst_str)
        # print(lnode.to_html())
        self.assertEqual(lst_str, node_str)

    def test2layer(self):
        item1 = LeafNode('li', 'First item')
        item2 = LeafNode('li', 'Second item')
        lnode = ParentNode('ol', [item1, item2])
        desc = LeafNode('p', 'i explain the list here')
        node = ParentNode('div', [desc, lnode], {'background-color': 'red'})
        node_str = "<div background-color=red>\n<p>i explain the list here</p>\n<ol>\n<li>First item</li>\n<li>Second item</li>\n</ol>\n</div>"
        nodehtml = node.to_html()
        # print(node_str)
        self.assertEqual(node_str, nodehtml)


if __name__ == "__main__":
    unittest.main()
