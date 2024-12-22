YOLOV11 = {
    'detect': {
        'nano': 'yolo11n.pt',
        'small': 'yolo11s.pt',
        'medium': 'yolo11m.pt',
        'large': 'yolo11l.pt',
        'xlarge': 'yolo11x.pt',
    },
    'segmentation': {
        'nano': 'yolo11n-seg.pt',
        'small': 'yolo11s-seg.pt',
        'medium': 'yolo11m-seg.pt',
        'large': 'yolo11l-seg.pt',
        'xlarge': 'yolo11x-seg.pt',
    },
    'pose': {
        'nano': 'yolo11n-pose.pt',
        'small': 'yolo11s-pose.pt',
        'medium': 'yolo11m-pose.pt',
        'large': 'yolo11l-pose.pt',
        'xlarge': 'yolo11x-pose.pt',
    },
    'orientedDetection':
        {
            'nano': 'yolo11n-obb.pt',
            'small': 'yolo11s-obb.pt',
            'medium': 'yolo11m-obb.pt',
            'large': 'yolo11l-obb.pt',
            'xlarge': 'yolo11x-obb.pt',
        },
    'classification': {
        'nano': 'yolo11n-cls.pt',
        'small': 'yolo11s-cls.pt',
        'medium': 'yolo11m-cls.pt',
        'large': 'yolo11l-cls.pt',
        'xlarge': 'yolo11x-cls.pt',
    }
}

YOLOV10 = {
    'objectDetection': {
        'nano': 'yolov10n.pt',
        'small': 'yolov10s.pt',
        'medium': 'yolov10m.pt',
        'large': 'yolov10l.pt',
        'xlarge': 'yolov10x.pt'
    }
}

YOLOV9 = {
    'objectDetection': {
        'nano': 'yolov9t.pt',
        'small': 'yolov9s.pt',
        'medium': 'yolov9m.pt',
        'large': 'yolov9c.pt',
        'xlarge': 'yolov9e.pt'
    },
    'instanceSegmentation': {
        'large': 'yolov9c-seg.pt',
        'xlarge': 'yolov9e-seg.pt'
    }
}

YOLOV8 = {
    'detect': {
        'nano': 'yolov8n.pt',
        'small': 'yolov8s.pt',
        'medium': 'yolov8m.pt',
        'large': 'yolov8l.pt',
        'xlarge': 'yolov8x.pt',
    },
    'segmentation': {
        'nano': 'yolov8n-seg.pt',
        'small': 'yolov8s-seg.pt',
        'medium': 'yolov8m-seg.pt',
        'large': 'yolov8l-seg.pt',
        'xlarge': 'yolov8x-seg.pt',
    },
    'pose': {
        'nano': 'yolov8n-pose.pt',
        'small': 'yolov8s-pose.pt',
        'medium': 'yolov8m-pose.pt',
        'large': 'yolov8l-pose.pt',
        'xlarge': 'yolov8x-pose.pt',
    },
    'orientedDetection':
        {
            'nano': 'yolov8n-obb.pt',
            'small': 'yolov8s-obb.pt',
            'medium': 'yolov8m-obb.pt',
            'large': 'yolov8l-obb.pt',
            'xlarge': 'yolov8x-obb.pt',
        },
    'classification': {
        'nano': 'yolov8n-cls.pt',
        'small': 'yolov8s-cls.pt',
        'medium': 'yolov8m-cls.pt',
        'large': 'yolov8l-cls.pt',
        'xlarge': 'yolov8x-cls.pt',
    }
}

YOLOV6 = {
    'detect': {
        'nano': 'yolov6-n.pt',
        'small': 'yolov6-s.pt',
        'medium': 'yolov6-m.pt',
        'large': 'yolov6-l.pt',
        'xlarge': 'yolov6-l6.pt',
    }
}

YOLOV5 = {
    'detect': {
        'nu': 'yolov5nu.pt',
        'su': 'yolov5su.pt',
        'mu': 'yolov5mu.pt',
        'lu': 'yolov5lu.pt',
        'xu': 'yolov5xu.pt',
        'n6u': 'yolov5n6u.pt',
        's6u': 'yolov5s6u.pt',
        'm6u': 'yolov5m6u.pt',
        '16u': 'yolov516u.pt',
        'x6u': 'yolov5x6u.pt',
    }
}

YOLO_MODELS = {11: YOLOV11, 10: YOLOV10,
               9: YOLOV9, 8: YOLOV8,
               6: YOLOV6, 5: YOLOV5, }

COCO = {
    'detect': {'coco': 'coco.yaml'},
    'segmentation': {'coco': 'coco.yaml'},
    'pose': {'coco': 'coco-pose.yaml'}
}
COCO8 = {
    'detect': {'coco8': 'coco8.yaml'},
    'segmentation': {'coco8': 'coco8-seg.yaml'},
    'pose': {'coco8': 'coco8-pose.yaml'}
}
DATASETS = {
    'coco': COCO,  # we need to fix it
    'coco8': COCO8,
}
