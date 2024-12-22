from ultralytics import YOLO
from config import YOLO_MODELS, DATASETS


class Yolo:
    def __init__(self, version, task, size):
        self.dataset_path = None
        self.version = version
        model_path = YOLO_MODELS[self.version]
        self.task = task
        model_path = model_path[self.task]
        self.size = size
        model_path = model_path[self.size]
        self.model = YOLO(model_path)

    def get_info(self):
        print(f'yolo version: {self.version}')
        print(f'yolo task: {self.task}')
        print(f'model size: {self.size}')
        print(self.model.info())

    def train(self, dataset, epochs=100, imgsz=640):
        dataset_path = DATASETS[dataset]
        dataset_path = dataset_path[self.task]
        dataset_path = dataset_path[dataset]
        self.dataset_path = dataset_path
        self.model.train(data=dataset_path, epochs=epochs, imgsz=imgsz)

    def fine_tune(self):
        pass

    def predict(self):
        pass

    def export(self):
        pass

    def evaluate(self):
        pass

    def validate(self):
        pass


# Instantiate the Yolo class
yolo = Yolo(version=11, task='detect', size='xlarge')
yolo.get_info()
yolo.train(dataset='coco')
