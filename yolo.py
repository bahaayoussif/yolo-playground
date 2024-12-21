from ultralytics import YOLO
from config import YOLO_MODELS


class Yolo:
    def __init__(self, version, task, size):
        version = YOLO_MODELS[version]
        task = version[task]
        model_path = task[size]
        self.model = YOLO(model_path)

    def get_info(self):
        print(self.model.info())

    def train(self):
        pass

    def fine_tune(self):
        pass

    def predict(self):
        pass


# Instantiate the Yolo class
yolo = Yolo(version=11, task='detect', size='nano')
yolo.get_info()