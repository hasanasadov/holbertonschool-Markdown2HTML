#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name """

import sys
import os

def markdown_to_html(markdown_text):
    html_text= ''
    html_text1= ''
    html_text2= ''
    html_text3= ''
    html_text4= ''
    lines = markdown_text.split('\n')
    in_ordered_list = False
    in_list = False
    in_paragraph = False


    for line in lines:
        if line.startswith('# '):
            html_text1 += f'<h1>{line[2:]}</h1>\n'
        elif line.startswith('## '):
            html_text1 += f'<h2>{line[3:]}</h2>\n'
        elif line.startswith('### '):
            html_text1 += f'<h3>{line[4:]}</h3>\n'
        elif line.startswith('#### '):
            html_text1 += f'<h4>{line[5:]}</h4>\n'
        elif line.startswith('##### '):
            html_text1 += f'<h5>{line[6:]}</h5>\n'
        elif line.startswith('###### '):
            html_text1 += f'<h6>{line[7:]}</h6>\n'
    html_text+=html_text1


    for line in lines:
        if line.startswith('- '):
            if not in_list:
                html_text2 += '<ul>\n'
                in_list = True
            html_text2 += f'    <li>{line[2:]}</li>\n'
        else:
            if in_list:
                html_text2 += '</ul>\n'
                in_list = False
    
    html_text+=html_text2

    for line in lines:
        if line.startswith('* '):
            if not in_ordered_list:
                html_text3 += '<ol>\n'
                in_ordered_list = True
            html_text3 += f'    <li>{line[2:]}</li>\n'
        else:
            if in_ordered_list:
                html_text3 += '</ol>\n'
                in_ordered_list = False

    html_text+=html_text3

    for line in lines:
        if line.strip() and line[+1].strip():
             
            


    return html_text




if __name__ == "__main__":
    markdown_text = """
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6

- Hello
- Bye

* Hello
* Bye

Hello

I'm a text
with 2 lines
    """
    html_output = markdown_to_html(markdown_text)
    print(html_output)


'''
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

markdown_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)
'''

#sys.exit(0)
