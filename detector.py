from ultralytics import YOLO
from config import yolo_model

'''model name in this .py is Model_'''
Model_ = YOLO(yolo_model)


'''--------source detect/process it into a "results"----------'''
#pic
def DetectPic(pic):
    results = Model_(pic)
    return results

#video
def DetectFrame(frame):
    results = Model_(frame)
    return results

