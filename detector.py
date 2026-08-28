from ultralytics import YOLO
from config import yolo_model

'''--------------重置器-----------------'''
def ResetTrack():
    global VideoModel_
    VideoModel_ = YOLO(yolo_model)


'''model name in this .py is Model_'''
PicModel_ = YOLO(yolo_model)
ResetTrack()#要想办法避免track污染。。。


'''--------source detect/process it into a "results"----------'''
#pic
def DetectPic(pic):
    results = PicModel_(pic)
    return results

#video
def DetectFrame(frame):
    #视频识别需要追踪
    results = VideoModel_.track(frame,persist=True,tracker="bytetrack.yaml")#persist=True: 标识track任务持续存在，不要每帧都重置id
    return results