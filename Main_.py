import detector,player
import event
from analyzer import AnalyzeResultsToItemsNamesList_pic,AnalyzeResultsToItemsNamesList_video
from config import yolo_source_pic,yolo_source_video,yolo_source_VF
from detector import DetectFrame
from event import check_event_pic, check_event_video
from processor import video_process, VideosInDir
from visualizer import show_box


def pic_execute(pic_path):
    resu = detector.DetectPic(pic_path)
    item_name_list = AnalyzeResultsToItemsNamesList_pic(resu)
    for name in item_name_list:
        if check_event_pic(name):
            player.play_sound_pic(name)


def video_execute(video_path):
    detector.ResetTrack()
    event.ResetEvent_TwoList()
    video_generator = video_process(video_path)
    frame_id = 0#暂时没啥用。。。
    #every frame：
    # 视频一帧里只有一个图-->results里只有一个results[0]
    for Frame in video_generator:#迭代器内循环
        resu = DetectFrame(Frame)
        frame_id = frame_id + 1
        show_box(Frame,resu)
        item_NameID_list = AnalyzeResultsToItemsNamesList_video(resu)
        for obj in item_NameID_list:
            name = obj["name"]
            id = obj["id"]
            conf = obj["conf"]
            if check_event_video(name,id,conf):
                player.play_sound_video(name)


#文件夹里多个视频循环，每一个新视频都要重置一下track，防止污染
def videos_folder_execute(folder_path):
    VideoPathList = VideosInDir(folder_path)
    for video_path in VideoPathList:
        video_execute(video_path)




#main:
#video_execute(yolo_source_video)
#pic_execute(yolo_source_pic)
videos_folder_execute(yolo_source_VF)