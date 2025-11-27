import sys

from copy_contents import copy_contents
from generate_page import generate_pages_recursive


def main():
    basepath = "/"
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]

    copy_contents("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()