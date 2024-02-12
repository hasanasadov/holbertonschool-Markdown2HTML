#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name """

import sys
import os
import hashlib
import re

def To_HTML(name,text):
    return "<"+name+">"+text+"</"+name+">\n"

def Heading(line):    
    count = line.count('#')
    name = "H"+str(count)
    return To_HTML(name,line[count+1:])

def UO_List(lines,name):
    text = ""
    for line in lines:
        text += "\t" + To_HTML("li",line[2:])
    return To_HTML(name,"\n" + text)

def Paragraph(lines):
    text = ""
    for line in lines:
        if(line!=lines[0]):
            text +='<br/>'
        text += '\n\t' + line + '\n'  
    return To_HTML('p',text)

def GetLines(lines,char = '', IsAlpha = False):
    L = [Bold(Em(SQ_brackets(Brackets(lines[0]))))]
    lines.remove(lines[0])
    while(len(lines) != 0):
        line = lines[0]
        if(line==''):
            break
        if((line[0].isalpha and IsAlpha) or line[0] == char):
            lines.remove(line)
            line = Bold(Em(SQ_brackets(Brackets(line))))
            L.append(line)
        else: 
            break
    return L

def Bold(line):
    line = re.sub("\*\*","<b>",line,1)
    line = re.sub("\*\*","</b>",line,1)
    return line

def Em(line):
    line = re.sub("__","<em>",line,1)
    line = re.sub("__","</em>",line,1)
    return line

def SQ_brackets(line):
    id = line.find("[[")
    id2 = line.find("]]")
    if(id!=-1 and id2!=-1):
        text = line[id+2:id2]
        line = line[:id] + str(hashlib.md5(text.encode()).hexdigest())+ line[id2+2:]
    return line

def Brackets(line):
    id = line.find("((")
    id2 = line.find("))")
    if(id!=-1 and id2!=-1):
        text = line[id+2:id2]
        text = text.replace('c','')
        text = text.replace('C','')
        line = line[:id] + text + line[id2+2:]
    return line
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)
    with open(sys.argv[1]) as IN:
        with open(sys.argv[2], 'w') as OUT:
            lines = IN.read().splitlines()
            html = ""
            
            while(len(lines) != 0):
                line = lines[0]
                if(line == ""):
                    lines.remove(line)
                else:
                    line = Bold(Em(SQ_brackets(Brackets(line))))
                    
                    if(line[0]=="#"):
                        html += Heading(line)
                        del lines[0]
                    elif(line[0]=='-'):
                        L = GetLines(lines,'-')
                        html += UO_List(L,"ul")        
                    elif(line[0]=='*'):
                        L = GetLines(lines,'*')
                        html += UO_List(L,"ol")
                    elif(line[0].isalpha):
                        L = GetLines(lines, IsAlpha = True)
                        html += Paragraph(L)
            OUT.write(html)
    exit(0)
