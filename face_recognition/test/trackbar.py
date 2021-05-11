import cv2


def test():
    cv2.namedWindow('tracks')
    cv2.createTrackbar("block_size", "tracks", 11, 300, lambda x: None)
    cv2.createTrackbar("cc", "tracks", 50, 200, lambda x: None)
    while True:
        block_size = cv2.getTrackbarPos("block_size", "tracks")
        cc = cv2.getTrackbarPos("cc", "tracks")
        block_size = block_size * 2 + 1
        cc = -cc
        print("block_size:{}===cc:{}" .format(str(block_size),str(cc)) )
        k = cv2.waitKey(1)
        if k == 27:
            break


if __name__ == '__main__':
    test()
