from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == "text" or text_node.text_type == "text_type_text":
            return LeafNode(None,text_node.text)
        elif text_node.text_type == "bold" or text_node.text_type == "text_type_bold":
            return LeafNode("b", text_node.text)
        elif text_node.text_type == "italic" or text_node.text_type == "text_type_italic":
            return LeafNode("i", text_node.text)
        elif text_node.text_type == "code" or text_node.text_type == "text_type_code":
            return LeafNode("code", text_node.text)
        elif text_node.text_type == "link" or text_node.text_type == "text_type_link":
            return LeafNode("a", text_node.text, props={"href":text_node.url})
        elif text_node.text_type == "image" or text_node.text_type == "text_type_image":
            return LeafNode("img", "", props={"src":text_node.url,"alt":text_node.text})
        raise ValueError(f"Invalid text type: {text_node.text_type}")