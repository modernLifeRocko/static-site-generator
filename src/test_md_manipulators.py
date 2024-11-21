import unittest

from md_manipulators import split_nodes_delimiter
from textnode import TextNode


class NodeSplitTest(unittest.TestCase):
    def testinlinebold(self):
        node = TextNode('this is *important*, i think', 'text')
        split_nodes = split_nodes_delimiter([node], '*', 'bold')
        goal = [
            TextNode('this is ', 'text'),
            TextNode('important', 'bold'),
            TextNode(', i think', 'text')
        ]
        self.assertEqual(split_nodes, goal)

    def testinlinecodeend(self):
        node = TextNode('look at my `code`', 'text')
        split_nodes = split_nodes_delimiter([node], '`', 'code')
        goal = [
            TextNode('look at my ', 'text'),
            TextNode('code', 'code')
        ]
        self.assertEqual(goal, split_nodes)

    def testitalicstart(self):
        node = TextNode('_cursive_ is cursed', 'text')
        split_nodes = split_nodes_delimiter([node], '_', 'italic')
        goal = [
            TextNode('cursive', 'italic'),
            TextNode(' is cursed', 'text')
        ]
        self.assertEqual(goal, split_nodes)

    def testmultibold(self):
        node = TextNode('This *is* important. So is *this*', 'text')
        split_nodes = split_nodes_delimiter([node], '*', 'bold')
        goal = [
            TextNode('This ', 'text'),
            TextNode('is', 'bold'),
            TextNode(' important. So is ', 'text'),
            TextNode('this', 'bold')
        ]
        self.assertEqual(goal, split_nodes)
