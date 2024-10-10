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
