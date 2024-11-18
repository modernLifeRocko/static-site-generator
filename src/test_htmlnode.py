import unittest

from htmlnode import HTMLNode


class HTMLNodeTest(unittest.TestCase):
    def testpropsnochild(self):
        node = HTMLNode('p', 'this is a paragraph', None,
                        {'color': 'black', 'margin': 'auto'})
        print(node)
        propsstr = node.props_to_html()
        self.assertEqual(propsstr, ' color= black margin= auto')

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
        self.assertEqual(pstr, ' margin= auto')
