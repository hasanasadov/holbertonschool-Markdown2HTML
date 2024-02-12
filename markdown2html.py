#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name """

import sys
import os
import hashlib
import re

if len(sys.argv) < 3: 
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)
#salma
markdown_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)


sys.exit(0)
