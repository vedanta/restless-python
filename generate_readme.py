import os
import re

def extract_comment(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        if match:
            return match.group(1).strip()
    return "No description available"

def generate_readme():
    notebooks = []
    for file in os.listdir('.'):
        if file.endswith('.ipynb'):
            py_file = file.replace('.ipynb', '.py')
            if os.path.exists(py_file):
                comment = extract_comment(py_file)
            else:
                comment = "No description available"
            notebooks.append((file, comment))

    with open('README.md', 'w') as readme:
        readme.write("# Jupyter Notebooks\n\n")
        readme.write("| Notebook | Description | Open in Colab |\n")
        readme.write("|----------|-------------|---------------|\n")
        for notebook, comment in notebooks:
            colab_badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/{os.environ['GITHUB_REPOSITORY']}/blob/main/{notebook})"
            readme.write(f"| {notebook} | {comment} | {colab_badge} |\n")

if __name__ == "__main__":
    generate_readme()