import os
import shutil
import random


s = './1'
d = './2'
cnt = 200
f = os.listdir(s)
random.shuffle(f)


for _ in f:
    if not cnt:
        break
    shutil.move(os.path.join(s, _), os.path.join(d, _))
    cnt -= 1
