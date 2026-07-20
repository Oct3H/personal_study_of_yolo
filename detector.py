from ultralytics import YOLO
from config import yolo_model


Model_ = YOLO(yolo_model)

def detector_source(source):
    results = Model_(source)
    return results
