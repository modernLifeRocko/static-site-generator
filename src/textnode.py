from htmlnode import LeafNode


text_types_dir = {
    "text": None,
    "bold": 'b',
    "italic": 'i',
    "code": 'code',
    "link": 'a',
    "image": 'img'
}


class TextNode():
    def __init__(self, text: str, text_type: str, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, o):
        # defines equality of text nodes as equality of all their properties
        isTextSame = self.text == o.text
        isTypeSame = self.text_type == o.text_type
        isUrlSame = self.url == o.url

        return isTextSame and isTypeSame and isUrlSame

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type not in text_types_dir:
        raise ValueError

    if text_node.text_type == 'image':
        return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})

    if text_node.text_type == 'link':
        return LeafNode('a', text_node.text, {'href': text_node.url})

    return LeafNode(text_types_dir[text_node.text_type], text_node.text)
