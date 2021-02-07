import numpy as np
from PIL import Image
import os
import cv2

"""
人脸数据训练
"""
base_path = os.path.dirname(os.__file__)


class Training:
    def __init__(self, face_path):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector = cv2.CascadeClassifier(
            os.path.join(base_path, r"site-packages\cv2\data\haarcascade_frontalface_default.xml"))
        self.face_path = face_path

    def start(self):
        print('Training faces. It will take a few seconds. Wait ...')
        faces, ids = self.get_images_and_labels(self.face_path)
        self.recognizer.train(faces, np.array(ids))
        self.recognizer.write(r'face_trainer\trainer.yml')
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
            id_pre = os.path.split(imagePath)[-1].split(".")[0]
            print("id_pre", id_pre)
            id = int(id_pre)
            faces = self.detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y + h, x: x + w])
                ids.append(id)
        return face_samples, ids


if __name__ == '__main__':
    train = Training(r'face_data\user1')
    train.start()
