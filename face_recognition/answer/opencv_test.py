import cv2 as cv


def mouse_click(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("mouse_click======EVENT_LBUTTONDOWN", event, x, y)


def deal_image():  # 图片处理
    # 加载一个图片到opencv中
    img = cv.imread('t1.png')
    print('img.shape===', img.shape)
    roi = img[205:614, 133:449]
    cv.imshow("origin", img)
    cv.imshow("resize", roi)
    cv.setMouseCallback('origin', mouse_click)
    cv.waitKey(0)


if __name__ == '__main__':
    deal_image()
