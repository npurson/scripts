import os
import json
import shutil
from tqdm import tqdm


root_dir = '/Users/89378/Downloads/yxs'
dst_dir = './yx'


def listfile(rootdir):
    _files = []
    list = os.listdir(rootdir)
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isdir(path):
            _files.extend(listfile(path))
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == '.json':
                _files.append(path)
    return _files


def is_contain_chinese(string):
    for ch in string:
        if '\u4e00' <= ch <= '\u9fa5':
            return True
    return False


def get_substr_idx(string, substr):
    return string.find(substr)


for _ in os.listdir(root_dir):
    try:
        cnt = 0
        src_dir = os.path.join(root_dir, _)
        if not os.path.isdir(src_dir):
            continue
        json_files = listfile(src_dir)
    except:
        print(_)
        os.system("pause")
        continue
    for filename in tqdm(json_files):
        try:
            f = open(os.path.join(src_dir, filename), encoding = 'utf-8')
        except FileNotFoundError:
            print('file not found')
            cnt += 1
            continue
        except LookupError:
            print('unknown encoding')
            cnt += 1
            continue
        except UnicodeDecodeError:
            print('decode error')
            cnt += 1
            continue
        
        try:
            j = json.load(f)
        except:
            print(filename)
            cnt += 1
            continue
        f.close()
        # if not is_contain_chinese(j["imagePath"]):
        #     continue
        try:
            img_path = j["imagePath"]
        except:
            print(filename)
            os.system("pause")
            continue
        # imgPath = imgPath[get_substr_idx(imgPath, "violation"):]
        try:
            if os.path.exists(os.path.join(src_dir, img_path)):
                if j["flags"]["压线"] and j["flags"]["逆行"]:
                        shutil.copyfile(os.path.join(src_dir, img_path), os.path.join(dst_dir, "yn", img_path))
                elif not j["flags"]["压线"] and j["flags"]["逆行"]:
                        shutil.copyfile(os.path.join(src_dir, img_path), os.path.join(dst_dir, "01", img_path))
                elif j["flags"]["压线"] and not j["flags"]["逆行"]:
                        shutil.copyfile(os.path.join(src_dir, img_path), os.path.join(dst_dir, "10", img_path))
                elif j["flags"]["无违规"]:
                        shutil.copyfile(os.path.join(src_dir, img_path), os.path.join(dst_dir, "00", img_path))
                elif j["flags"]["无法判断"]:
                        shutil.copyfile(os.path.join(src_dir, img_path), os.path.join(dst_dir, "un", img_path))
                else:
                    cnt += 1
            else :
                cnt += 1
        except:
            print(filename)
            continue
print(cnt)
os.system("pause")
