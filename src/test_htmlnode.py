import unittest

from htmlnode import HTMLNode, LeafNode


class HTMLNodeTest(unittest.TestCase):
    def testpropsnochild(self):
        node = HTMLNode('p', 'this is a paragraph', None,
                        {'color': 'black', 'margin': 'auto'})
        print(node)
        propsstr = node.props_to_html()
        self.assertEqual(propsstr, ' color=black margin=auto')

    def testnopropschild(self):
        node1 = HTMLNode('li', 'first list item')
        node2 = HTMLNode('li', 'second list item')

        listnode = HTMLNode('ol', None, [node1, node2])
        print(listnode)

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
        node = LeafNode('div', '', {'margin': 'auto', 'background-color': 'blue'})
        node_str='<div margin=auto background-color=blue></div>'
        print(node.to_html())
        self.assertEqual(node_str, node.to_html())
