import os
import re
import markdown
import pdfkit
from mdx_math import MathExtension

def find_markdown_files(directory):
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return sorted(markdown_files, key=lambda x: os.path.basename(x))

def markdown_to_html(markdown_file):
    with open(markdown_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    def image_handler(match):
        image_path = match.group(1)
        abs_image_path = os.path.abspath(os.path.join(os.path.dirname(markdown_file), image_path))
        return f'<img src="{abs_image_path}" alt="Image">'
    
    md_content = re.sub(r'!\[\[(.*?)\]\]', image_handler, md_content)
    
    md = markdown.Markdown(extensions=['extra', MathExtension(enable_dollar_delimiter=True)])
    
    html_content = md.convert(md_content)
    
    html_content = html_content.replace('$$', '\\[', 1)
    html_content = html_content.replace('$$', '\\]', 1)
    
    return html_content

def combine_html(html_contents):
    mathjax_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>'
    combined_html = f'''
    <html>
    <head>
        <meta charset="UTF-8">
        {mathjax_cdn}
        <script type="text/x-mathjax-config">
            MathJax.Hub.Config({{
                tex2jax: {{
                    inlineMath: [['$','$']],
                    displayMath: [['$$','$$']],
                    processEscapes: true
                }},
                "HTML-CSS": {{ 
                    linebreaks: {{ automatic: true }},
                    scale: 100,
                    styles: {{
                        ".MathJax_Display": {{
                            "text-align": "center !important"
                        }}
                    }}
                }}
            }});
        </script>
        <style>
            @font-face {{
                font-family: 'CMU Serif';
                font-weight: normal;
                font-style: normal;
            }}
            body {{
                font-family: 'CMU Serif', serif;
                font-size: 12pt;
                line-height: 1.6;
                margin: 0;
                padding: 0;
            }}
            .file-content {{
                page-break-after: always;
            }}
            .page {{
                position: relative;
                padding: 2cm 2cm 2cm 2cm;
                box-sizing: border-box;
                min-height: 24.61cm;
            }}
            .page-number {{
                position: absolute;
                bottom: 2cm;
                right: 2cm;
                font-size: 12pt;
            }}
            .MathJax_Display, .MJXc-display, .MathJax_SVG_Display {{
                display: flex !important;
                justify-content: center !important;
                align-content: center !important;
                align-items: center !important;
                margin: 1em 0 !important;
            }}
            img {{
                max-width: 100%;
                height: auto;
            }}
            blockquote {{
                border: 1px solid black;
                padding: 16px;
            }}
            @media print {{
                @page {{    
                    size: A4;
                    margin: 0;
                }}
                body {{
                    margin: 0;
                }}
                .file-content {{
                    page-break-after: always;
                }}
                .page {{
                    page-break-after: always;
                    padding: 0cm 2cm 0cm 2cm;
                }}
                
            }}
            
        </style>
    </head>
    <body>
    '''
    for html in html_contents:
        combined_html += f'''
        <div class="file-content">
            <div class="page">
                {html}
            </div>
        </div>
        '''

    combined_html += '''
    
    </body></html>
    '''
    return combined_html

def main():
    current_dir = os.getcwd()
    markdown_files = find_markdown_files(current_dir)
    
    if not markdown_files:
        print("No Markdown files found in the current directory or its subdirectories.")
        return

    html_contents = [markdown_to_html(file) for file in markdown_files]
    combined_html = combine_html(html_contents)
    
    output_file = os.path.join(current_dir, 'combined_markdown.pdf')
    
    options = {
        'encoding': 'UTF-8',
        'enable-local-file-access': None,
        'javascript-delay': 2000,
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }
    
    open(f'{current_dir}.html', 'w', encoding='utf-8').write(combined_html)

    # pdfkit.from_string(combined_html, output_file, options=options)
    # print(f"PDF file has been created: {output_file}")

if __name__ == "__main__":
    main()