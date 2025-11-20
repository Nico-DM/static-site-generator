from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_blocktype(text):
    if any([ text.startswith(f"{'#' * i} ") for i in range(1, 7) ]):
        return BlockType.HEADING
    elif text.startswith("```") and text.endswith("```"):
        return BlockType.CODE
    elif all(map(lambda line: line.startswith(">"), text.splitlines())):
        return BlockType.QUOTE
    elif all(map(lambda line: line.startswith("- "), text.splitlines())):
        return BlockType.UNORDERED_LIST
    elif all(map(lambda line: line[1].startswith(f"{line[0] + 1}. "), enumerate(text.splitlines()))):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH