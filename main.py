import re

def convert_markdown(md_text):
    # Removing Headings
    md_text = re.sub(r'^#\s+(.+)$', r'\\section{\1}', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^##\s+(.+)$', r'\\subsection{\1}', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^###\s+(.+)$', r'\\subsubsection{\1}', md_text, flags=re.MULTILINE)

    # Change Citations
    md_text = re.sub(r'\[@([^\]]+)\]', r'\\citep{\1}', md_text)
    
    # Bold and Italic 2 Textbf, Textit
    md_text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', md_text)
    md_text = re.sub(r'\*(.+?)\*', r'\\textit{\1}', md_text)
    
    return md_text

# Read input
input_file_path = 'input.md'
output_file_path = 'output.tex'

with open(input_file_path, 'r') as input_file:
    md_content = input_file.read()

converted_text = convert_markdown(md_content)

# Save
with open(output_file_path, 'w') as output_file:
    output_file.write(converted_text)

print("Conversion complete. Output saved to", output_file_path)
