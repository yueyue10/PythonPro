import os

if __name__ == '__main__':
    base_path = os.path.dirname(os.__file__)
    ss = os.path.join(base_path, 'site-packages\cv2\data\haarcascade_frontalface_default.xml')
    print(ss)
