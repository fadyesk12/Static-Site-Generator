block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ul = "unordered_list"
block_type_ol = "ordered_list"

from htmlnode import *
from leafnode import *
from parentnode import *
from inline_markdown import *
from textnode import text_node_to_html_node

def markdown_to_blocks(markdown):
    print("a3")
    blocks = markdown.split("\n\n")
    newBlocks = []
    for block in blocks:
        newBlocks.append(block.strip())
    return newBlocks

def block_to_block_type(block):
    lines = block.split("\n")
    if block[0] == "#":
        for c in range(len(block)):
            if block[c] == "#" and block[c+1] == " ":
                return block_type_heading

    elif block.startswith("```") and block.endswith("```"):
        return block_type_code

    quote = False
    for line in lines:
        if line.startswith("> "):
            quote = True
            continue
        quote = False
        break
    if quote:
        return block_type_quote
    
    ul = False
    for line in lines:
        if line.startswith("* ") or line.startswith("- "):
            ul = True
            continue
        ul = False
        break
    if ul:
        return block_type_ul

    count = 1
    ol = False
    for line in lines:
        if line.startswith(f"{count}. "):
            ol = True
            count+=1
            continue
        ol = False
        break
    if ol:
        return block_type_ol

    return block_type_paragraph


def paragraph_to_HTML(block):
    lines = block.split("\n")
    children = []
    textnodes = text_to_textnodes(block)
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    resultNode = ParentNode("p",children)
    # return "<p>" + block + "</p>"
    return resultNode

def heading_to_HTML(block):
    count = 0
    for char in range(len(block)):
        if block[char] == "#":
            count += 1
        else:
            break
    lines = block.split("\n")
    newLines = []
    stripped = ""
    for i in range(count):
        stripped += "#"
    for line in lines:
        newLines.append(line.strip(f"{stripped} "))

    result = "\n".join(newLines)
    children = []
    textnodes = text_to_textnodes(result)
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    resultNode = ParentNode(f"h{count}",children)
    return resultNode
    # result = "\n".join(newLines)
    # return f"<h{count}>" + result + f"</h{count}>"
def code_to_HTML(block):
    lines = block.split("\n")
    newLines = []
    for line in lines:
        newLines.append(line.strip(" ``` "))
    result = "\n".join(newLines)
    children = []
    textnodes = text_to_textnodes(result)
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    codeNode = ParentNode("code",children)
    resultNode = ParentNode("pre",[codeNode])
    return resultNode
    # result = "\n".join(newLines)
    # return "<pre><code>" + result + "</code></pre>"

def quote_to_HTML(block):
    lines = block.split("\n")
    newLines = []
    for line in lines:
        newLines.append(line.strip("> "))
    result = "\n".join(newLines)
    children = []
    textnodes = text_to_textnodes(result)
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    resultNode = ParentNode("blockquote", children)
    return resultNode
    # return "<blockquote>" + result + "</blockquote>"

def ul_to_HTML(block):
    # resultHTML = "<ul>"
    lines = block.split("\n")
    newLines = []
    for line in lines:
        newline = line.strip("- ")
        newLines.append(newline.strip("* "))
    # for line in newLines:
    #     resultHTML += "<li>" + line + "</li>"
    children = []
    for line in newLines:
        listItemChildren = []
        nodes = text_to_textnodes(line)
        for node in nodes:
            listItemChildren.append(text_node_to_html_node(node))
        children.append(ParentNode("li",listItemChildren))
    resultNode = ParentNode("ul", children)
    return resultNode
    # return resultHTML + "</ul>"

def ol_to_HTML(block):
    resultHTML = "<ol>"
    lines = block.split("\n")
    newLines = []
    count = 1
    for line in lines:
        stripped = f"{count}. "
        newline = line.strip(stripped)
        newLines.append(newline)
        count+=1
    children = []
    for line in newLines:
        listItemChildren = []
        nodes = text_to_textnodes(line)
        for node in nodes:
            listItemChildren.append(text_node_to_html_node(node))
        children.append(ParentNode("li",listItemChildren))
    resultNode = ParentNode("ol", children)
    return resultNode
    # for line in newLines:
    #     resultHTML += "<li>" + line + "</li>"
    # return resultHTML + "</ol>"

def block_to_HTML(block, block_type):
    if block_type == block_type_heading:
        return heading_to_HTML(block)
    elif block_type == block_type_code:
        return code_to_HTML(block)
    elif block_type == block_type_quote:
        return quote_to_HTML(block)
    elif block_type == block_type_ul:
        return ul_to_HTML(block)
    elif block_type == block_type_ol:
        return ol_to_HTML(block)
    return paragraph_to_HTML(block)

def markdown_to_HTML(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_HTML(block,block_to_block_type(block)))
    return ParentNode("div", children)