from textnode import TextNode
import re


def split_nodes_delimiter(old_nodes: list[TextNode],
                          delimiter: str,
                          text_type: str) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        txt = node.text
        slices = txt.split(delimiter)
        if node.text_type != 'text':
            new_nodes.append(node)
            continue

        if len(slices) % 2 == 0:
            raise ValueError('Invalid md')

        for i, slice in enumerate(slices):
            if slice != '':
                if i % 2 == 0:
                    new_nodes.append(TextNode(slice, 'text'))
                else:
                    new_nodes.append(TextNode(slice, text_type))

    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pat = r'!\[(.+?)\]\((.+?)\)'
    return re.findall(pat, text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pat = r'[^!]\[(.+?)\]\((.+?)\)'
    return re.findall(pat, text)


# def split_nodes_delimiter2(old_nodes: list[TextNode],
#                           delimiter: str,
#                           text_type: str) -> list[TextNode]:
#     new_nodes = []
#     for node in old_nodes:
#         txt = node.text
#         txt_type = node.text_type
#         fst_idx = txt.find(delimiter)
#         if fst_idx == -1:
#             new_nodes += [node]
#         else:
#             if fst_idx != 0:
#                 new_nodes += [TextNode(txt[:fst_idx], txt_type)]
#             lst_idx = fst_idx + txt[fst_idx+1:].find(delimiter) + 1
#             new_nodes += [TextNode(txt[fst_idx+1:lst_idx], text_type)]
#             if lst_idx != len(txt)-1:
#                 new_nodes += split_nodes_delimiter(
#                     [TextNode(txt[lst_idx+1:], txt_type)],
#                     delimiter, text_type)
#     return new_nodes
