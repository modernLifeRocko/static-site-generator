class HTMLNode():
    def __init__(self, tag: str | None = None,
                 value: str | None = None,
                 children: list | None = None,
                 props: dict[str, str] | None = None):
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list | None = children
        self.props: dict[str, str] | None = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        propstr = ""
        if self.props is None:
            return propstr
        for key, val in self.props.items():
            propstr += f" {key}={val}"
        return propstr

    def __repr__(self):
        return f'''
        tag: {self.tag}
        value: {self.value}
        children: {self.children}
        props: {self.props_to_html()}'''


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None,
                 value: str,
                 props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return self.value

        if self.tag == 'img':
            return f'<{self.tag}{self.props_to_html()}/>'
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
