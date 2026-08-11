from ultralytics import YOLO
from config import yolo_model



'''--------------重置器-----------------'''
#要想办法避免多个视频连续播放导致（如果一直是同一个track的话）track污染。。。
def ResetTrack():
    VideoModel_ = YOLO(yolo_model)
    return VideoModel_



'''model name in this .py is Model_'''
PicModel_ = YOLO(yolo_model)
#VideoModel_ = YOLO(yolo_model)
VideoModel_ = ResetTrack()#要想办法避免track污染。。。


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

