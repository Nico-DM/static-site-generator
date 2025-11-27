import os

from markdown_to_html_node import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith('# '):
            return line.lstrip('#').strip()
        if line:
            break
    raise ValueError("No title found in the markdown content.")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page (using {template_path}):")
    print(f"\t{from_path}")
    print(f"\t{dest_path}")

    with open(from_path, "r") as f:
        content = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    page = (template
            .replace("{{ Title }}", title)
            .replace("{{ Content }}", html)
            .replace('href="/', f'href="{basepath}')
            .replace('src="/', f'src="{basepath}')
            )

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as f:
        f.write(page)

def generate_pages_recursive(content_dir, template_file, public_dir, basepath):
    for entry in os.listdir(content_dir):
        from_path = os.path.join(content_dir, entry)
        dest_path = os.path.join(public_dir, entry)

        if os.path.isfile(from_path):
            generate_page(from_path, template_file, dest_path.rstrip(".md") + ".html", basepath)
        else:
            generate_pages_recursive(from_path, template_file, dest_path, basepath)