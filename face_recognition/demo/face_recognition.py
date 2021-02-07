import os

import cv2

from demo import conf

"""
人脸检测
"""


class Recognition:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(conf.train_path)
        self.faceCascade = cv2.CascadeClassifier(
            os.path.join(conf.base_path, r"site-packages\cv2\data\haarcascade_frontalface_default.xml"))
        self.cam = cv2.VideoCapture(0)

    def start(self):
        min_w = 0.1 * self.cam.get(3)
        min_h = 0.1 * self.cam.get(4)
        font = cv2.FONT_HERSHEY_SIMPLEX
        face_dict = conf.face_dict

        while True:
            ret, img = self.cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(min_w), int(min_h))
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                f_id, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])
                print("recognizer.predict", f_id, confidence)
                if confidence < 100:
                    face_name = face_dict[str(f_id)]
                    confidence = "{0}%".format(round(100 - confidence))
                else:
                    face_name = "unknown"
                    confidence = "{0}%".format(round(100 - confidence))

                cv2.putText(img, str(face_name), (x + 5, y - 5), font, 1, (0, 0, 255), 1)
                cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (0, 0, 0), 1)
            cv2.imshow('camera', img)
            k = cv2.waitKey(10)
            if k == 27:
                break
        self.destroy()

    def destroy(self):
        self.cam.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    recognition = Recognition()
    recognition.start()
