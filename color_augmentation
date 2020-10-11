import numpy as np
import cv2
import os
from tqdm import tqdm


src_dir = '../data/train_pic'
dst_dir = '../data/train_aug'


def convert_image(image,cvt_type):
    if cvt_type == 'HSV':
        return cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    elif cvt_type == 'HSL':
        return cv2.cvtColor(image,cv2.COLOR_RGB2HLS)  # h l s


def select_color(image):
    cvt_image = convert_image(image, 'HSL')
    # yellow mask
    yellow_lower = np.uint8([10, 0, 100])  # h l s
    yellow_upper = np.uint8([40, 255, 255]) 
    yellow_mask = cv2.inRange(cvt_image, yellow_lower, yellow_upper)
    # white mask
    white_lower = np.array([0,200,0])
    white_upper = np.array([255, 255, 255])
    white_mask = cv2.inRange(cvt_image, white_lower, white_upper)
    # combine mask
    mask = cv2.bitwise_or(yellow_mask,white_mask)
    return cv2.bitwise_and(image,image,mask=mask)


def main():
    for f in tqdm(os.listdir(src_dir)):
        img = select_color(cv2.imread(os.path.join(src_dir, f)))
        cv2.imwrite(os.path.join(dst_dir, f), img)


if __name__ == '__main__':
    main()
