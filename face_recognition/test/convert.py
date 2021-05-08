# -*- coding: utf-8 -*-
import cv2
import numpy as np
from imutils import contours
from imutils.perspective import four_point_transform


def test():
    # 载入并显示图片
    img = cv2.imread('t3.jpg')
    img = cv2.resize(img, (500, 700), 0, 0)
    # 1.降噪（模糊处理用来减少瑕疵点）
    result = cv2.blur(img, (5, 5))
    # 2.灰度化,就是去色（类似老式照片）
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # 霍夫变换圆检测
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=250, param2=15, minRadius=2, maxRadius=20)
    circles = np.round(circles[0, :]).astype('int')
    print("circles1", circles)
    four_points = []
    for (x, y, r) in circles:
        # 绘制圆和半径矩形到output
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)
        four_points.append([x, y])
    # 透视变换
    rect = four_point_transform(gray, np.array(four_points))
    rect_img = four_point_transform(img, np.array(four_points))
    # 显示新图像
    cv2.imshow('circle', img)
    cv2.imshow('rect_img', rect_img)
    # 按任意键退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test()
