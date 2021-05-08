# -*- coding: utf-8 -*-
import cv2
import numpy as np


def test():
    # 载入并显示图片
    img = cv2.imread('t3.jpg')
    # # 定义想要缩放后的图片大小
    info = img.shape  # 获取图片的宽 高 颜色通道信息
    dst_width = int(info[1] * 0.2)
    dst_height = int(info[0] * 0.2)
    img = cv2.resize(img, (500, 700), 0, 0)

    cv2.imshow('1', img)
    # 降噪（模糊处理用来减少瑕疵点）
    result = cv2.blur(img, (5, 5))
    cv2.imshow('2', result)
    # 灰度化,就是去色（类似老式照片）
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    cv2.imshow('3', gray)

    # param1的具体实现，用于边缘检测
    canny = cv2.Canny(img, 40, 80)
    cv2.imshow('4', canny)

    # 霍夫变换圆检测
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, param1=250, param2=15, minRadius=2, maxRadius=20)
    # 输出返回值，方便查看类型
    print(circles)
    # cv2.waitKey(0)

    # 输出检测到圆的个数
    print(len(circles[0]))

    print('-------------我是条分割线-----------------')
    # 方法一：复杂
    # 根据检测到圆的信息，画出每一个圆
    # for circle in circles[0]:
    #     # 圆的基本信息
    #     print(circle[2])
    #     # 坐标行列(就是圆心)
    #     x = int(circle[0])
    #     y = int(circle[1])
    #     # 半径
    #     r = int(circle[2])
    #     # 在原图用指定颜色圈出圆，参数设定为int所以圈画存在误差
    #     img = cv2.circle(img, (x, y), r, (0, 0, 255), 1, 8, 0)
    # 方法二：简单一点
    circles = np.round(circles[0, :]).astype('int')
    for (x, y, r) in circles:
        # 绘制圆和半径矩形到output
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)
    # 显示新图像
    cv2.imshow('5', img)

    # 按任意键退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test()
