import os

import cv2

"""
人脸检测
"""

base_path = os.path.dirname(os.__file__)


class Recognition:
    def __init__(self, train_path):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(train_path)
        self.faceCascade = cv2.CascadeClassifier(
            os.path.join(base_path, r"site-packages\cv2\data\haarcascade_frontalface_default.xml"))
        self.cam = cv2.VideoCapture(0)

    def start(self):
        idnum = 0
        min_w = 0.1 * self.cam.get(3)
        min_h = 0.1 * self.cam.get(4)
        font = cv2.FONT_HERSHEY_SIMPLEX
        names = ['Allen', 'zyj', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7']

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
                idnum, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])
                print("recognizer.predict", idnum, confidence)
                if confidence < 100:
                    # print("idnum", idnum)
                    idnum = "user1"
                    confidence = "{0}%".format(round(100 - confidence))
                else:
                    idnum = "unknown"
                    confidence = "{0}%".format(round(100 - confidence))

                cv2.putText(img, str(idnum), (x + 5, y - 5), font, 1, (0, 0, 255), 1)
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
    recognition = Recognition('face_trainer/trainer.yml')
    recognition.start()
