#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def detectCircles():
    # 加载图像
    image = cv2.imread('t1.png')

    output = image.copy()
    # 转换成灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 检测圆
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 20)
    # 确保至少找到一个圆
    if circles is not None:
        # 将圆(x, y)坐标和半径转换成int
        circles = np.round(circles[0, :]).astype('int')
        for (x, y, r) in circles:
            # 绘制圆和半径矩形到output
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        cv2.imshow('output', np.hstack([image, output]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    detectCircles()
