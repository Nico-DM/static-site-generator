from block_to_blocktype import block_to_blocktype, BlockType
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_html import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


def blocktype_to_html_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return ParentNode("p", text_to_children(block.replace("\n", " ")))
        case BlockType.HEADING:
            hashes, text = block.split(" ", maxsplit = 1)
            return ParentNode(f"h{len(hashes)}", text_to_children(text))
        case BlockType.CODE:
            return ParentNode("pre", [ParentNode("code", [text_node_to_html_node(TextNode(block.strip("`\n"), TextType.TEXT))])])
        case BlockType.QUOTE:
            new_text = ""
            for line in block.splitlines():
                new_text += line[2:] + "\n"
            new_text = new_text.rstrip("\n")
            return ParentNode("blockquote", text_to_children(new_text))
        case BlockType.UNORDERED_LIST:
            list_items = []
            for line in block.splitlines():
                list_items.append(ParentNode("li", text_to_children(line[2:])))
            return ParentNode("ul", list_items)
        case BlockType.ORDERED_LIST:
            list_items = []
            for line in block.splitlines():
                list_items.append(ParentNode("li", text_to_children(line.split(". ", maxsplit = 1)[1])))
            return ParentNode("ol", list_items)
        case _:
            raise ValueError("Unsupported block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(map(lambda node: text_node_to_html_node(node), text_nodes))

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        node = blocktype_to_html_node(block, block_type)
        nodes.append(node)
    return ParentNode("div", nodes)