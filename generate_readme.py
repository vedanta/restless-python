import os
import json
import nbformat

def extract_description(notebook_file):
    with open(notebook_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    if len(nb.cells) > 0 and nb.cells[0].cell_type == 'markdown':
        content = nb.cells[0].source
        if content.startswith('# Description'):
            description = content.split('\n', 1)[1].strip()
            # Remove leading colon if present
            return description[1:].strip() if description.startswith(':') else description
    
    return "No description available"

def generate_readme():
    notebooks = []
    for file in os.listdir('.'):
        if file.endswith('.ipynb'):
            # Check if corresponding Python file exists
            py_file = file[:-6] + '.py'
            if os.path.exists(py_file):
                description = extract_description(file)
                notebooks.append((file, description))
            else:
                print(f"Warning: {file} doesn't have a corresponding Python file. Skipping...")

    with open('README.md', 'w') as readme:
        readme.write("# Jupyter Notebooks\n\n")
        if notebooks:
            readme.write("| Notebook | Description | Open in Colab |\n")
            readme.write("|----------|-------------|---------------|\n")
            for notebook, description in notebooks:
                colab_link = f"https://colab.research.google.com/github/{os.environ['GITHUB_REPOSITORY']}/blob/main/{notebook}"
                colab_badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_link})"
                readme.write(f"| {notebook} | {description} | {colab_badge} |\n")
        else:
            readme.write("No notebooks available at the moment.\n")

    print("README.md has been generated successfully.")

if __name__ == "__main__":
    generate_readme()