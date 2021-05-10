# -*- coding: utf-8 -*-
from operator import attrgetter, itemgetter

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
    circles = cv2.HoughCircles(gray.copy(), cv2.HOUGH_GRADIENT, 1, 200, param1=250, param2=15, minRadius=2,
                               maxRadius=20)
    circles = np.round(circles[0, :]).astype('int')

    # 排序circles坐标
    # print("circles1===", circles)
    circles2 = sorted(circles, key=lambda x: x[1])  # 对y轴排序
    # print("circles2", circles2)
    top_list = sorted(circles2[0: 2], key=lambda x: x[0])  # 对x轴排序
    bottom_list = sorted(circles2[2: 4], key=lambda x: x[0])  # 对x轴排序
    circles3 = np.vstack((top_list, bottom_list))
    # print("circles3", circles3)

    four_points = []
    for idx, (x, y, r) in enumerate(circles3):
        # 绘制圆和半径矩形到output
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)
        if idx == 0:
            four_points.append([x + r, y + r])
        elif idx == 1:
            four_points.append([x - r, y + r])
        elif idx == 2:
            four_points.append([x + r, y - r])
        elif idx == 3:
            four_points.append([x - r, y - r])
    # 透视变换
    gray_trans = four_point_transform(gray, np.array(four_points))
    img_trans = four_point_transform(img, np.array(four_points))
    # 显示新图像
    cv2.imshow('circle', img)
    cv2.imshow('rect_img', img_trans)
    transform(gray_trans, img_trans)
    # 按任意键退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def transform(gray_trans, img_trans):
    gaussian_bulr = cv2.GaussianBlur(gray_trans, (5, 5), 0)
    cv2.imshow("gaussian", gaussian_bulr)
    edged = cv2.Canny(gaussian_bulr, 75, 200)  # 边缘检测,灰度值小于2参这个值的会被丢弃，大于3参这个值会被当成边缘，在中间的部分，自动检测
    cv2.imshow("edged", edged)
    # 寻找轮廓
    image, cts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    path_list = []
    for c in cts:
        peri = 0.01 * cv2.arcLength(c, True)
        path_list.append({"c": c, "peri": peri})
    # print("path_list", path_list)
    path_sort = sorted(path_list, key=lambda x: x['peri'], reverse=True)
    # print("path_sort", path_sort)

    # 给轮廓加标记，便于我们在原图里面观察，注意必须是原图才能画出红色，灰度图是没有颜色的
    # cv2.drawContours(rect, [path_sort[0]['c']], -1, (0, 0, 255), 3)
    # cv2.imshow("draw_contours", gray_trans)

    x, y, w, h = cv2.boundingRect(path_sort[0]['c'])
    cv2.rectangle(gray_trans, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("rectangle", gray_trans)
    # print("rect.shape()", rect.shape)
    my, mx = gray_trans.shape

    four_points = [[0, y + h], [mx, y + h], [0, my], [mx, my]]
    gray_trans2 = four_point_transform(gray_trans, np.array(four_points))
    img_trans2 = four_point_transform(img_trans, np.array(four_points))
    cv2.imshow("img_trans2", img_trans2)
    answer(gray_trans2, img_trans2)


def answer(gray_trans2, img_trans2):
    thresh2 = cv2.adaptiveThreshold(gray_trans2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 50)
    cv2.imshow("ostu2", thresh2)
    r_image, r_cnt, r_hierarchy = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("找到轮廓个数----------------：", len(r_cnt), r_cnt)
    # 使用红色标记所有的轮廓
    # cv2.drawContours(img_trans2, r_cnt, -1, (0, 0, 255), 2)
    # 把所有找到的轮廓，给标记出来
    question_cts = []
    for cxx in r_cnt:
        # 通过矩形，标记每一个指定的轮廓
        x, y, w, h = cv2.boundingRect(cxx)
        ar = w / float(h)
        if w >= 5 and w < 10:
            cv2.rectangle(img_trans2, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # 把每个选项，保存下来
            question_cts.append(cxx)
    print("question_cts========", len(question_cts))
    cv2.imshow("ox_1", img_trans2)


if __name__ == '__main__':
    test()

    # path_list = [{'name': 'A', 'value': 1}, {'name': 'B', 'value': 2}, {'name': 'C', 'value': 3}]
    # path_sort = sorted(path_list, key=lambda x:x['value'],reverse=True)
    # print("path_sort", path_sort)