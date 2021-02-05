import numpy as np
from PIL import Image
import os
import cv2

"""
人脸数据训练
"""
# 人脸数据路径
data_path = r'E:\Users\Python\PythonPro\face_recognition\demo\facedata\user1'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(r"E:\Users\Python\Libs\FaceIdentify\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")


def getImagesAndLabels(path):
    image_paths = []
    for f in os.listdir(path):
        print(f)
        image_paths.append(os.path.join(path, f))
    print("image_paths", image_paths)
    face_samples = []
    ids = []
    for imagePath in image_paths:
        PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
        img_numpy = np.array(PIL_img, 'uint8')
        id_pre = os.path.split(imagePath)[-1].split(".")[0]
        print("id_pre", id_pre)
        id = int(id_pre)
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            face_samples.append(img_numpy[y:y + h, x: x + w])
            ids.append(id)
    return face_samples, ids


print('Training faces. It will take a few seconds. Wait ...')
faces, ids = getImagesAndLabels(data_path)
recognizer.train(faces, np.array(ids))

recognizer.write(r'face_trainer\trainer.yml')
print("{0} faces trained. Exiting Program".format(len(np.unique(ids))))
