from weasyprint import HTML
import os

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths
html_path = os.path.join(script_dir, 'index.html')
css_path = os.path.join(script_dir, 'styles.css')
pdf_path = os.path.join(script_dir, 'seminar-plan.pdf')

# Read CSS separately to ensure it's applied
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Create HTML with embedded CSS
html_content = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <style>{css_content}</style>
</head>
<body>
'''

# Read the body content from index.html
with open(html_path, 'r', encoding='utf-8') as f:
    full_html = f.read()
    # Extract body content
    body_start = full_html.find('<body>') + 6
    body_end = full_html.find('</body>')
    body_content = full_html[body_start:body_end]

html_content += body_content + '</body></html>'

# Generate PDF
HTML(string=html_content).write_pdf(pdf_path)

print(f'PDF generated: {pdf_path}')
