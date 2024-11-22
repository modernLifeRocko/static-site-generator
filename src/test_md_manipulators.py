import unittest

from md_manipulators import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link
)

from textnode import TextNode


class NodeSplitTest(unittest.TestCase):
    def testinlinebold(self):
        node = TextNode('this is **important**, i think', 'text')
        split_nodes = split_nodes_delimiter([node], '**', 'bold')
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
        node = TextNode('This **is** important. So is **this**', 'text')
        split_nodes = split_nodes_delimiter([node], '**', 'bold')
        goal = [
            TextNode('This ', 'text'),
            TextNode('is', 'bold'),
            TextNode(' important. So is ', 'text'),
            TextNode('this', 'bold')
        ]
        self.assertEqual(goal, split_nodes)


class ImgXtractTest(unittest.TestCase):
    def test1img(self):
        mdtxt = 'See this ![photo](img/to/pic). Cute right?'
        imgs = [('photo', 'img/to/pic')]
        self.assertEqual(imgs, extract_markdown_images(mdtxt))

    def test2img(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        imgs = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(imgs, extract_markdown_images(text))


class LinkXtractTest(unittest.TestCase):
    def testnoimg(self):
        mdtxt = 'See this ![photo](img/to/pic). Cute right?'
        self.assertEqual([], extract_markdown_links(mdtxt))

    def test1link(self):
        mdtxt = 'Go [here](https://en.wikipedia.org/wiki/Never_Gonna_Give_You_Up)'
        links = [
            ('here', 'https://en.wikipedia.org/wiki/Never_Gonna_Give_You_Up')
        ]
        self.assertEqual(links, extract_markdown_links(mdtxt))

    def test2link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = [("to boot dev", "https://www.boot.dev"),
                 ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(links, extract_markdown_links(text))


class SplitImgsTest(unittest.TestCase):
    def test1img(self):
        node1 = TextNode(
            'see this: ![alt text](dir/to/img)', 'text')
        goal = [
            TextNode('see this: ', 'text'),
            TextNode('', 'image', {'alt': 'alt text', 'src': 'dir/to/img'})
        ]
        self.assertEqual(goal, split_nodes_image([node1]))

    def testnoimg(self):
        node = TextNode('watch my [guns](dir/to/guns]', 'text')
        goal = [node]
        self.assertEqual(goal, split_nodes_image([node]))


class SplitLinxTest(unittest.TestCase):
    def testnolink(self):
        node1 = TextNode(
            'see this: ![alt text](dir/to/img)', 'text')
        goal = [
            node1
        ]
        self.assertEqual(goal, split_nodes_link([node1]))

    def test2links(self):
        node = TextNode('see [here](file) or [here](file2)', 'text')
        goal = [
            TextNode('see ', 'text'),
            TextNode('here', 'link', {'href': 'file'}),
            TextNode(' or ', 'text'),
            TextNode('here', 'link', {'href': 'file2'})
        ]
        self.assertEqual(goal, split_nodes_link([node]))

    def testlistlinks(self):
        node1 = TextNode('see [this](file) for more.', 'text')
        node2 = TextNode('or go [here](file2) for even more', 'text')
        goal = [
            TextNode('see ', 'text'),
            TextNode('this', 'link', {'href': 'file'}),
            TextNode(' for more.', 'text'),
            TextNode('or go ', 'text'),
            TextNode('here', 'link', {'href': 'file2'}),
            TextNode(' for even more', 'text')
        ]
        self.assertEqual(goal, split_nodes_link([node1, node2]))


if __name__ == "__main__":
    unittest.main()
