"""
人脸识别功能测试
"""
import os


class Config:
    base_path = os.path.dirname(os.__file__)
    train_path = 'face_trainer/trainer.yml'
    face_path = "face_data"
    width = 640
    height = 480
    h_wid = int(width / 2)
    h_hei = int(height / 2)

    def get_face_dict(self):
        img_paths = []
        face_dict = {}  # 人脸字典 id-name
        path = self.face_path
        for f in os.listdir(path):
            img_paths.append(os.path.join(path, f))
        # print("img_paths", img_paths)
        for img_path in img_paths:
            img_name = os.path.split(img_path)[-1]
            face_name = img_name.split(".")[0]
            face_id = img_name.split(".")[1]
            face_dict[face_id] = face_name
        return face_dict

    def get_face_paths(self):
        image_paths = []
        for f in os.listdir(self.face_path):
            image_paths.append(os.path.join(self.face_path, f))
        return image_paths

    def get_face_images(self):
        face_images = []
        for f_path in self.get_face_paths():
            with open(f_path, 'rb') as f:
                img = f.read()
                # img = base64.b64encode(f.read())
                face_images.append(img)
        return face_images


conf = Config()
