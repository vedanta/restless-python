
import os
import re

def extract_description(py_file):
    with open(py_file, 'r') as file:
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
                description = extract_description(py_file)
            else:
                description = "No description available"
            notebooks.append((file, description))

    with open('README.md', 'w') as readme:
        readme.write("# Jupyter Notebooks\n\n")
        readme.write("| Notebook | Description | Open in Colab |\n")
        readme.write("|----------|-------------|---------------|\n")
        for notebook, description in notebooks:
            colab_link = f"https://colab.research.google.com/github/{os.environ['GITHUB_REPOSITORY']}/blob/main/{notebook}"
            colab_badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_link})"
            readme.write(f"| {notebook} | {description} | {colab_badge} |\n")

    print("README.md has been generated successfully.")

if __name__ == "__main__":
    generate_readme()