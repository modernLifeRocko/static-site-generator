from textnode import TextNode


def main():
    text = "This is a dummy text"
    text_type = "bold"
    url = "https://www.boot.dev/"
    dummy = TextNode(text, text_type, url)
    print(dummy)


if __name__ == '__main__':
    main()
