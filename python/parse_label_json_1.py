import os
import json
import shutil
from tqdm import tqdm


src_dir = '/data/Traffic_datas/7006TrainAndValid'
dst_dir = '/data/jhy/7006'
json_dir = '/data/Traffic_datas/LabeledJsonFile/7006'
json_files = listfile(json_dir)


def listfile(rootdir):
    _files = []
    list = os.listdir(rootdir)
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isdir(path):
            _files.extend(listfile(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files


def is_contain_chinese(string):
    for ch in string:
        if '\u4e00' <= ch <= '\u9fa5':
            return True
    return False


def get_substr_idx(string, substr):
    return string.find(substr)


for filename in tqdm(json_files):
    f = open(os.path.join(json_dir, filename), encoding = 'utf-8')
    try:
        j = json.load(f)
    except:
        continue
    f.close()
    flag = False
    if not is_contain_chinese(j["imagePath"]):
        continue
    img_path = j["imagePath"]
    # imgPath = imgPath[get_substr_idx(imgPath, "violation"):]
    # print(imgPath.encode("utf-8"))
    for _ in ["train/INVALID/0", "train/INVALID/1", "train/INVALID/2", "train/INVALID/3", "train/INVALID/4", "train/VALID/0", "train/VALID/1", "valid/INVALID", "valid/VALID"]:
        if os.path.exists(os.path.join(src_dir, _, img_path)):
            if j["flags"]["INVALID"] and not j["flags"]["VALID"]:
                shutil.copyfile(os.path.join(src_dir, _, img_path), os.path.join(dst_dir, "INVALID", img_path))
            elif not j["flags"]["INVALID"] and j["flags"]["VALID"]:
                shutil.copyfile(os.path.join(src_dir, _, img_path), os.path.join(dst_dir, "VALID", img_path))
            flag = True
            break
    if not flag:
        for _ in ["valid/INVALID", "valid/VALID"]:
            if os.path.exists(os.path.join(src_dir, _, j["imagePath"])):
                if j["flags"]["INVALID"] and not j["flags"]["VALID"]:
                    shutil.copyfile(os.path.join(src_dir, _, img_path), os.path.join(dst_dir, "INVALID", img_path))
                elif not j["flags"]["INVALID"] and j["flags"]["VALID"]:
                    shutil.copyfile(os.path.join(src_dir, _, img_path), os.path.join(dst_dir, "VALID", img_path))
                flag = True
                break
