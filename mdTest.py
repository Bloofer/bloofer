import markdown
import codecs
import sys
 
md = markdown.Markdown()
 
html_header = '''
<html>
<head>
<link href="github.css" rel="stylesheet"></link>
</head>
<body>
<div class="markdown-body">
'''
 
html_footer = '''
</div>
</body>
</html>
'''
 
 
def convert():
    # input file (*.md)
    md_file = codecs.open("test.md",encoding='utf-8',mode="r")
    code = markdown.markdown(md_file.read())
 
    # output file (input.md.html)
    html_file = codecs.open("test.html",encoding='utf-8',mode="w")
    html_file.write(html_header + code + html_footer)


convert()
