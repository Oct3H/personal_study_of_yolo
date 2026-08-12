from ultralytics import YOLO
from config import yolo_model



#error example：
#                                       要想办法避免多个视频连续播放导致（如果一直是同一个track的话）track污染。。。
#                                       老版本：如果在detector里确实没问题，但问题是main！ 这个函数是靠返回值重置模型的，但是main里面“接不住”
#                                      或者说，接住了，但是return到main里，在这个文件里没有意义，因此应该用「global+无返回值函数」才行
'''                                         def ResetTrack():
                                            VideoModel_ = YOLO(yolo_model)
                                            return VideoModel_
                                            
                                            
                                            
                                            VideoModel_ = ResetTrack()
'''


'''--------------重置器-----------------'''
def ResetTrack():
    global VideoModel_
    VideoModel_ = YOLO(yolo_model)



'''model name in this .py is Model_'''
PicModel_ = YOLO(yolo_model)
#VideoModel_ = YOLO(yolo_model)
#VideoModel_ = ResetTrack()
#要想办法避免track污染。。。




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

