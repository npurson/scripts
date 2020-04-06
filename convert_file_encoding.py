import os
import sys
import codecs

s_dir = './1'
f_type = '.json'
input_encoding = 'gb2312'
output_encoding = 'utf-8'

def readFile(file, encoding):
    with codecs.open(file, 'r', encoding) as f:
        return f.read()

def writeFile(file,u,encoding):
    with codecs.open(file, 'w', encoding) as f:
        f.write(u)

def convert(f):
    print(f)
    content = readFile(f, input_encoding)
    writeFile(f, content, output_encoding)

files = os.listdir(s_dir)
for f in files:
    if os.path.splitext(f)[1] == f_type:
        convert(os.path.join(s_dir, f))
