from sympy.physics.units import metric_ton
from ultralytics import YOLO
from config import YOLO_MODELS, DATASETS


class Yolo:
    def __init__(self, version, task, size):
        self.version = version
        model_path = YOLO_MODELS[self.version]
        self.task = task
        model_path = model_path[self.task]
        self.size = size
        model_path = model_path[self.size]
        self.model = YOLO(model_path)
        self.dataset_path = None
        self.metrics = None

    def get_info(self):
        print(f'yolo version: {self.version}')
        print(f'yolo task: {self.task}')
        print(f'model size: {self.size}')
        print(self.model.info())

    def train(self, dataset, epochs=100, imgsz=640, device='mps'):
        dataset_path = DATASETS[dataset]
        dataset_path = dataset_path[self.task]
        dataset_path = dataset_path[dataset]
        self.dataset_path = dataset_path
        print(f'dataset path: {dataset_path}')
        self.model.train(data=dataset_path, epochs=epochs, imgsz=imgsz, device=device)

    def fine_tune(self):
        pass

    def predict(self):
        pass

    def export(self, file_format):
        self.model.export(format=file_format)

    def evaluate(self):
        pass

    def validate(self, dataset=None):
        if dataset is None:
            self.metrics = self.model.val()
            print(self.metrics.box.map)
            print(self.metrics.box.map50)
            print(self.metrics.box.map75)
            print(self.metrics.box.maps)

        else:
            self.metrics = self.model.val(data=dataset)
            print(self.metrics.box.map)
            print(self.metrics.box.map50)
            print(self.metrics.box.map75)
            print(self.metrics.box.maps)


# Instantiate the Yolo class
yolo = Yolo(version=11, task='detect', size='xlarge')
yolo.get_info()
yolo.train(dataset='coco8', epochs=100)
yolo.export(file_format='coreml')
