#!/usr/bin/python3
import sys
import os
"""
salam
nlbfldk
shvu
"""
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
