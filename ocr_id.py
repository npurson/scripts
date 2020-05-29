import os
import cv2
import xlwt
from tqdm import tqdm
from aip import AipOcr
from collections import defaultdict

APP_ID = 'xxxxxxxx'
API_KEY = 'xxxxxxxx'
SECRET_KEY = 'xxxxxxxx'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def listdir(rootdir):
    _files = []
    list = os.listdir(rootdir)
    for i in range(len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isdir(path):
            _files.extend(listdir(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files


def image2text(img):
    dic_result = client.basicGeneral(img)
    result = str(dic_result['words_result'][0]['words'])
    return result


def ndarray2bytes(img):
    return cv2.imencode(".jpg", img)[1].tobytes()


def get_roi(filename):
    img = cv2.imread(filename)
    return img[0:288]
    # return img


def get_id(txt):
    i = 0
    j = 0
    for i in range(len(txt)):
        if '\u4e00' <= txt[i] <= '\u9fff':
            break
    for j in range(i, len(txt)):
        if txt[j] == '、':
            continue
        if not ('\u4e00' <= txt[j] <= '\u9fff'):
            break
    if j == len(txt) - 1:
        if '\u4e00' <= txt[j] <= '\u9fff':
            j += 1
    if txt[i:j][-2:] == '逆行':
        j -= 2
    if txt[i:j][-4:] == '车道行驶':
        j -= 6
    return txt[i:j]


total = 0
cnt = 0
cnt1 = 0
dict = defaultdict(int)
files = listdir('\\Users\\89378\\Downloads\\nx')

workbook = xlwt.Workbook(encoding = 'ascii')
sheet0 = workbook.add_sheet('sheet0')
sheet1 = workbook.add_sheet('sheet1')


for f in tqdm(files):
    try:
        cv2.imread(f)
    except:
        continue
    
    total += 1
    sheet0.write(total, 0, f.split('\\')[-1])
    
    try:
        txt = image2text(ndarray2bytes(get_roi(f)))
    except:
        continue

    if len(txt) <= 5:  # 返回字符串太短
        continue

    id = get_id(txt)
    if len(id) == 0:
        continue
    
    sheet0.write(total, 1, id)
    dict[id] += 1
    cnt += 1

    if cnt >= 50:
        break

for (k,v) in dict.items(): 
    sheet1.write(cnt1, 0, k)
    sheet1.write(cnt1, 1, v)
    cnt1 += 1

workbook.save('./1301.xls')
if not total == 0:
    print(cnt / total)
os.system('pause')