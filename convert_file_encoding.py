import os
import sys
import codecs
from tqdm import tqdm


s_dir = './1'
f_type = '.json'
input_encoding = 'gb2312'
output_encoding = 'utf-8'


def read_file(file, encoding):
    with codecs.open(file, 'r', encoding) as f:
        return f.read()


def write_file(file,u,encoding):
    with codecs.open(file, 'w', encoding) as f:
        f.write(u)


def convert(f):
    content = read_file(f, input_encoding)
    write_file(f, content, output_encoding)


files = os.listdir(s_dir)
for f in tqdm(files):
    if os.path.splitext(f)[1] == f_type:
        convert(os.path.join(s_dir, f))
# os.system('pause')
