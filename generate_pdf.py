from weasyprint import HTML, CSS
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

html_path = os.path.join(script_dir, 'index.html')
css_path = os.path.join(script_dir, 'styles.css')
pdf_path = os.path.join(script_dir, 'seminar-plan.pdf')

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

with open(html_path, 'r', encoding='utf-8') as f:
    full_html = f.read()

body_start = full_html.find('<body>') + 6
body_end = full_html.find('</body>')
body_content = full_html[body_start:body_end]

# Find the style tag content (Google Fonts link won't work in WeasyPrint, so we embed fonts via CSS)
html_content = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;600;700&display=swap');
    {css_content}
  </style>
</head>
<body>
{body_content}
</body>
</html>'''

HTML(string=html_content).write_pdf(
    pdf_path,
    presentational_hints=True,
)

print(f'PDF generated: {pdf_path}')
