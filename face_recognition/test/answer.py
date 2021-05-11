# -*- coding: utf-8 -*-
from operator import attrgetter, itemgetter

import cv2
import numpy as np
from imutils import contours
from imutils.perspective import four_point_transform

hor_space = 15  # 横向间距15
hor_que_space = 15  # 答案单个横向间距
ver_space = 15  # 纵向间距15
ver_que_space = 40  # 答案块纵向间距


class Answer(object):
    def __init__(self, path):
        self.path = path

    def start(self):
        ans_list = []  # 选择的题目和答案
        gray_trans, img_trans = self.read_img(self.path)
        gray_trans2, img_trans2 = self.transform_again(gray_trans, img_trans)
        sel_cts = self.get_sel_point(gray_trans2,img_trans2)
        card_list = self.get_card_list()  # 答题卡区域
        for que_item in sel_cts:
            ans_item = self.compute_score(que_item, img_trans2, card_list)
            ans_list.append(ans_item)
        print("ans_list", ans_list)
        return ans_list

    # 读取图片，根据四个定位圆进行透视变换
    def read_img(self, path):
        # 载入并显示图片
        img = cv2.imread(path)
        img = cv2.resize(img, (500, 700), 0, 0)
        # 1.降噪（模糊处理用来减少瑕疵点）
        result = cv2.blur(img, (5, 5))
        # 2.灰度化,就是去色（类似老式照片）
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        # 3.霍夫变换圆检测-定位答题卡圆圈位置
        circles = cv2.HoughCircles(gray.copy(), cv2.HOUGH_GRADIENT, 1, 200, param1=250, param2=15, minRadius=2,
                                   maxRadius=20)
        circles = np.round(circles[0, :]).astype('int')
        circles = sorted(circles, key=lambda x: x[1])  # 对y轴排序
        top_circles = sorted(circles[0: 2], key=lambda x: x[0])  # 对x轴排序
        bottom_circles = sorted(circles[2: 4], key=lambda x: x[0])  # 对x轴排序
        loc_circles = np.vstack((top_circles, bottom_circles))  # 重新组装的定位圆
        # 遍历4个定位圆，取出其有用的坐标
        four_points = []
        for idx, (x, y, r) in enumerate(loc_circles):
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
        # 根据定位圆的坐标进行透视变换
        gray_trans = four_point_transform(gray, np.array(four_points))
        img_trans = four_point_transform(img, np.array(four_points))
        # 显示新图像
        cv2.imshow('circle', img)
        cv2.imshow('rect_img', img_trans)
        return gray_trans, img_trans

    # 再次根据中间横线进行透视变换
    def transform_again(self, gray_trans, img_trans):
        gaussian_bulr = cv2.GaussianBlur(gray_trans, (5, 5), 0)
        cv2.imshow("gaussian", gaussian_bulr)
        edged = cv2.Canny(gaussian_bulr, 75, 200)  # 边缘检测,灰度值小于2参这个值的会被丢弃，大于3参这个值会被当成边缘，在中间的部分，自动检测
        cv2.imshow("edged", edged)
        # 1.寻找轮廓
        image, cts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 2.将轮廓数据以{c:轮廓，peri:周长}dict形式存放到path_list里面
        path_list = []
        for c in cts:
            peri = 0.01 * cv2.arcLength(c, True)
            path_list.append({"c": c, "peri": peri})
        # 3.对集合数据根据周长进行排序
        path_sort = sorted(path_list, key=lambda x: x['peri'], reverse=True)
        # print("path_sort", path_sort)
        # 显示排序第一个的轮廓数据
        # cv2.drawContours(rect, [path_sort[0]['c']], -1, (0, 0, 255), 3)
        # cv2.imshow("draw_contours", gray_trans)
        # 4.取轮廓的矩形坐标
        x, y, w, h = cv2.boundingRect(path_sort[0]['c'])
        cv2.rectangle(gray_trans, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("rectangle", gray_trans)
        # print("rect.shape()", rect.shape)
        my, mx = gray_trans.shape
        # 5.利用轮廓坐标组成新的透视定位4坐标点
        four_points = [[0, y + h], [mx, y + h], [0, my], [mx, my]]
        # 6.再次进行透视转换
        gray_trans2 = four_point_transform(gray_trans, np.array(four_points))
        img_trans2 = four_point_transform(img_trans, np.array(four_points))
        cv2.imshow("img_trans2", img_trans2)
        return gray_trans2, img_trans2

    # 获取选中的答案
    def get_sel_point(self, gray_trans2):
        thresh2 = cv2.adaptiveThreshold(gray_trans2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 50)
        cv2.imshow("ostu2", thresh2)
        r_image, r_cnt, r_hierarchy = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print("找到轮廓个数----------------：", len(r_cnt), r_cnt)
        # 使用红色标记所有的轮廓
        # cv2.drawContours(img_trans2, r_cnt, -1, (0, 0, 255), 2)
        # 把所有找到的轮廓，给标记出来
        sel_cts = []
        for cxx in r_cnt:
            # 通过矩形，标记每一个指定的轮廓
            x, y, w, h = cv2.boundingRect(cxx)
            ar = w / float(h)
            if 10 > w >= 5:
                # cv2.rectangle(img_trans2, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # 把每个选项，保存下来
                sel_cts.append([x, y, w, h])
        print("sel_cts========", len(sel_cts))
        return sel_cts

    # 计算分数
    def compute_score(self, que_item, img_trans2, card_list):
        # print("que=========", que_item)
        x, y, w, h = que_item
        cx = x + w / 2  # 中心x坐标
        cy = y + h / 2  # 中心y坐标
        # 便于调试，显示当前题目及答案
        cv2.rectangle(img_trans2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("ox_1", img_trans2)
        # print("key_list", key_list)
        choose_que = []
        for coo in card_list:
            x, y = coo['value']
            # print("coo", x, y)
            if x + hor_que_space > cx > x and y + ver_que_space > cy > y:
                choose_ans = self.get_answer(cy - y, ver_que_space)
                print("题目{},答案{}".format(coo['key'], choose_ans))
                choose_que = [coo['key'], choose_ans]
                break
        return choose_que

    @staticmethod
    def get_card_list():
        card_list = []
        for j in range(5):
            for i in range(20):
                hor_space_num = i // 5 + 1  # 所在横向块数
                hor_piece_num = (i + 1) % 5  # 所在横向份数
                start_x = (hor_space_num - 1) * hor_space + hor_que_space * i
                # if i == 5 and j == 0: print("hor_", hor_space_num, hor_piece_num, start_x)  # 横向的第几块，第几份
                start_y = j * ver_space + ver_que_space * j
                # if i == 0 and j == 4: print("纵向的第{}块，y坐标{}".format(j + 1, start_y))  # 纵向的第几块，第几份
                card_list.append({"key": j * 20 + (i + 1), "value": [start_x, start_y]})
        return card_list

    # 获取答案
    def get_answer(self, sel, all):
        percent = sel / all
        if percent < 1 / 5:
            return "num"
        elif percent < 2 / 5:
            return "A"
        elif percent < 3 / 5:
            return "B"
        elif percent < 4 / 5:
            return "C"
        elif percent < 1:
            return "D"


if __name__ == '__main__':
    answer = Answer("../answer/t3.jpg")
    answer.start()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
