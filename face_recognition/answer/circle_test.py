import cv2
import numpy as np
from PIL import Image
import cv2
import numpy as np
from cv2 import HoughCircles


def show_circle(path):
    img = cv2.imread(path)
    output = img.copy()

    # 定义想要缩放后的图片大小
    info = img.shape  # 获取图片的宽 高 颜色通道信息
    dst_width = int(info[1] * 0.2)
    dst_height = int(info[0] * 0.2)
    image = cv2.resize(img, (dst_width, dst_height), 0, 0)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray", gray)
    circles = HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100)
    print(len(circles))


if __name__ == '__main__':
    show_circle("t2.jpg")
