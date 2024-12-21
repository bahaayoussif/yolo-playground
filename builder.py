from ultralytics import YOLO
import cv2
from PIL import Image


class Builder:
    def __init__(self, model_name):
        models = {'yolo 3': 'source-models/yolov3.yaml',
                  'yolo 5': 'source-models/yolov5.yaml',
                  'yolo 6': 'source-models/yolov6.yaml',
                  'yolo 8': 'source-models/yolov8.yaml',
                  'yolo 9': 'source-models/yolov9m.yaml',
                  'yolo 10': 'source-models/yolov10x.yaml', }
        self.model_path = models[model_name]
        self.model = YOLO(self.model_path)

    def info(self):
        return self.model.info()

    def train(self, dataset_path, epochs):
        self.model.train(data=dataset_path, epochs=epochs)

    def validate(self, dataset_path=None):
        if dataset_path is None:
            self.model.val()
        else:
            self.model.val(data=dataset_path)

    def predict(self, image_path, save_image=True, save_text=True, multiple=False):
        if multiple:
            images = [Image.open(i_path) for i_path in image_path]
            results = self.model.predict(source=images, save_image=save_image, save_txt=save_text)
            return results
        else:
            image = Image.open(image_path)
            results = self.model.predict(source=image, save_image=save_image, save_txt=save_text)
            return results


model = Builder('yolo 10')
model.info()
