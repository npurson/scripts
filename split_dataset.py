import os
import random
import shutil

src_dir = ''
train_dir = ''
test_dir = ''
test_num = 3000

for dir in os.listdir(src_dir):
    if not os.path.isdir(os.path.join(src_dir, dir)):
        continue
    files = os.listdir(os.path.join(src_dir, dir))
    random.shuffle(files)
    cnt = 0
    for f in files:
        if cnt < test_num:
            shutil.move(os.path.join(src_dir, dir, f), os.path.join(test_dir, dir, f))
            cnt += 1
        else:
            shutil.move(os.path.join(src_dir, dir, f), os.path.join(train_dir, dir, f))
