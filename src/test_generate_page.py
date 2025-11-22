import unittest

from generate_page import generate_page


class TestGeneratePage(unittest.TestCase):
    def test_generate_page(self):
        from_path = "test_data/test_input.md"
        template_path = "test_data/test_template.html"
        dest_path = "test_data/test_output.html"

        # Create test input markdown file
        with open(from_path, "w") as f:
            f.write("# Test Title\n\nThis is a test paragraph.")

        # Create test template HTML file
        with open(template_path, "w") as f:
            f.write("<html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>")

        # Generate the page
        generate_page(from_path, template_path, dest_path)

        # Read the generated output
        with open(dest_path, "r") as f:
            output = f.read()

        expected_output = "<html><head><title>Test Title</title></head><body><div><h1>Test Title</h1><p>This is a test paragraph.</p></div></body></html>"

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()