import numpy as np
from PIL import Image
from demo import conf
import os
import cv2

"""
人脸数据训练
"""


class Training:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector = cv2.CascadeClassifier(
            os.path.join(conf.base_path, r"site-packages\cv2\data\haarcascade_frontalface_default.xml"))

    def start(self):
        print('Training faces. It will take a few seconds. Wait ...')
        faces, ids = self.get_images_and_labels(conf.face_path)
        self.recognizer.train(faces, np.array(ids))
        self.recognizer.write(conf.train_path)
        print("{0} faces trained. Exiting Program".format(len(np.unique(ids))))

    def get_images_and_labels(self, path):
        image_paths = []
        for f in os.listdir(path):
            image_paths.append(os.path.join(path, f))
        print("image_paths", image_paths)
        face_samples = []
        ids = []
        for imagePath in image_paths:
            pil_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(pil_img, 'uint8')
            face_id = os.path.split(imagePath)[-1].split(".")[1]
            print("id_pre", face_id)
            faces = self.detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y + h, x: x + w])
                ids.append(int(face_id))
        return face_samples, ids


if __name__ == '__main__':
    train = Training()
    train.start()
