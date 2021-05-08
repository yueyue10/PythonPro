from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import cv2 as cv

ANSWER_KEY_SCORE = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}
ANSWER_KEY = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}


def deal_image():  # 图片处理
    # 加载一个图片到opencv中
    img = cv.imread('t1.png')
    # 1.原图
    # cv.imshow("orgin", img)

    # 2.转化成灰度图片
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow("gray", gray)

    # 3.高斯模糊图
    gaussian_bulr = cv.GaussianBlur(gray, (5, 5), 0)
    # cv.imshow("gaussian", gaussian_bulr)

    # 4.使用边缘检测后的图
    edged = cv.Canny(gaussian_bulr, 75, 200)  # 边缘检测,灰度值小于2参这个值的会被丢弃，大于3参这个值会被当成边缘，在中间的部分，自动检测
    # cv.imshow("edged", edged)

    # 寻找轮廓
    image, cts, hierarchy = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # 给轮廓加标记，便于我们在原图里面观察，注意必须是原图才能画出红色，灰度图是没有颜色的
    cv.drawContours(img, cts, -1, (0, 0, 255), 3)

    # 按面积大小对所有的轮廓排序
    cts_sort = sorted(cts, key=cv.contourArea, reverse=True)
    print("寻找轮廓的个数：", len(cts_sort))  # 最外面的轮廓
    # cv.imshow("draw_contours", img)
    filter_rect_cts(cts_sort, img, gray)


def filter_rect_cts(cts_sort, img, gray):  # 筛选轮廓为矩形的区域
    # print(list)
    for c in cts_sort:
        # 周长，第1个参数是轮廓，第二个参数代表是否是闭环的图形
        peri = 0.01 * cv.arcLength(c, True)
        # 获取多边形的所有定点，如果是四个定点，就代表是矩形
        approx = cv.approxPolyDP(c, peri, True)
        # 打印定点个数
        print("顶点个数：", len(approx))
        if len(approx) == 4:  # 矩形
            # 透视变换提取原图内容部分
            ox_sheet = four_point_transform(img, approx.reshape(4, 2))
            # 透视变换提取灰度图内容部分
            tx_sheet = four_point_transform(gray, approx.reshape(4, 2))
            # cv.imshow("ox", ox_sheet)
            # cv.imshow("tx", tx_sheet)
            # 使用ostu二值化算法对灰度图做一个二值化处理
            ret, thresh2 = cv.threshold(tx_sheet, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
            cv.imshow("ostu", thresh2)
            filter_answer_cts(thresh2, ox_sheet, tx_sheet)
            break


def filter_answer_cts(thresh2, ox_sheet, tx_sheet):  # 筛选轮廓特征为答题选择区域
    # 继续寻找轮廓
    r_image, r_cnt, r_hierarchy = cv.findContours(thresh2.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    print("找到轮廓个数----------------：", len(r_cnt))
    # 使用红色标记所有的轮廓
    cv.drawContours(ox_sheet, r_cnt, -1, (0, 0, 255), 2)
    # 把所有找到的轮廓，给标记出来
    question_cts = []
    for cxx in r_cnt:
        # 通过矩形，标记每一个指定的轮廓
        x, y, w, h = cv.boundingRect(cxx)
        ar = w / float(h)
        if w >= 20 and h >= 20 and 0.9 <= ar <= 1.1:
            # 使用红色标记，满足指定条件的图形
            cv.rectangle(ox_sheet, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # 把每个选项，保存下来
            question_cts.append(cxx)
    print("question_cts========", question_cts)
    cv.imshow("ox_1", ox_sheet)
    com_answer_list(ox_sheet, tx_sheet, question_cts, thresh2)


def com_answer_list(ox_sheet, tx_sheet, question_cts, thresh2):  # 组合答题条目
    # 正确题的个数
    correct_count = 0
    # 按坐标从上到下排序
    sort_question_cts = contours.sort_contours(question_cts, method="top-to-bottom")[0]
    # 使用np函数，按5个元素，生成一个集合
    for (q, i) in enumerate(np.arange(0, len(sort_question_cts), 5)):
        # 获取按从左到右的排序后的5个元素
        com_question_cts = contours.sort_contours(sort_question_cts[i:i + 5])[0]
        choice_num = get_choose_answer_num(tx_sheet, thresh2, com_question_cts)
        fill_color = None
        # 如果做对就加1
        if ANSWER_KEY_SCORE.get(q) == choice_num:
            fill_color = (0, 255, 0)  # 正确 绿色
            correct_count = correct_count + 1
        else:
            fill_color = (0, 0, 255)  # 错误 红色
        cv.drawContours(ox_sheet, com_question_cts[choice_num], -1, fill_color, 2)
    cv.imshow("answer_flagged", ox_sheet)
    text1 = "total: " + str(len(ANSWER_KEY)) + ""
    text2 = "right: " + str(correct_count)
    text3 = "score: " + str(correct_count * 1.0 / len(ANSWER_KEY) * 100) + ""
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(ox_sheet, text1 + "  " + text2 + "  " + text3, (10, 30), font, 0.5, (0, 0, 255), 2)
    cv.imshow("score", ox_sheet)


def get_choose_answer_num(tx_sheet, thresh2, com_question_cts):  # 获取选中的答案
    bubble_rows = []
    # 遍历每一个选项
    for (j, c) in enumerate(com_question_cts):
        # 生成一个大小与透视图一样的全黑背景图布
        mask = np.zeros(tx_sheet.shape, dtype="uint8")
        # 将指定的轮廓+白色的填充写到画板上,255代表亮度值，亮度=255的时候，颜色是白色，等于0的时候是黑色
        cv.drawContours(mask, [c], -1, 255, -1)
        # 做两个图片做位运算，把每个选项独自显示到画布上，为了统计非0像素值使用，这部分像素最大的其实就是答案
        mask = cv.bitwise_and(thresh2, thresh2, mask=mask)
        # cv.imshow("c" + str(i), mask)
        # 获取每个答案的像素值
        total = cv.countNonZero(mask)
        # 存到一个数组里面，tuple里面的参数分别是，像素大小和答案的序号值
        # print(total,j)
        bubble_rows.append((total, j))
    bubble_rows = sorted(bubble_rows, key=lambda x: x[0], reverse=True)
    # 选择的答案序号
    choice_num = bubble_rows[0][1]
    print("答案：{} 数据: {}".format(ANSWER_KEY.get(choice_num), bubble_rows))
    return choice_num


if __name__ == '__main__':
    deal_image()
    cv.waitKey(0)
