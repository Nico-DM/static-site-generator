import os

from markdown_to_html_node import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith('# '):
            return line.lstrip('#').strip()
        if line:
            break
    raise ValueError("No title found in the markdown content.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        content = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as f:
        f.write(page)