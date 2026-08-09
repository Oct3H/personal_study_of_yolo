from ultralytics import YOLO
from config import yolo_model

'''model name in this .py is Model_'''
PicModel_ = YOLO(yolo_model)
VideoModel_ = YOLO(yolo_model)


'''--------source detect/process it into a "results"----------'''
#pic
def DetectPic(pic):
    results = PicModel_(pic)
    return results

#video
def DetectFrame(frame):
    #视频识别需要追踪
    results = VideoModel_.track(frame,persist=True)#persist=True: 标识track任务持续存在，不要每帧都重置id
    return results

