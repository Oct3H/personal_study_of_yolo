import detector,player
from analyzer import AnalyzeResultsToItemsNamesList_pic,AnalyzeResultsToItemsNamesList_video
from config import yolo_source_pic,yolo_source_video
from detector import DetectFrame
from event import check_event_pic,check_event_video
from processor import video_process, VideosInDir
from visualizer import show_box

'''-------------------------------------------------------------'''


'''
#功能组合执行(已废弃⚠️)
#single pic/series of pics AND single frame ALL CAN use it to analyze animals and return bark
def analyze_and_return_bark(A_Results):
    for pic in A_Results:
        for cls_number in pic.boxes.cls:#cls里的序号是「n.」，属于float；而names里的dict头是int，因此需要int化
            item_name = pic.names[int(cls_number)]
            player.play_sound(item_name)
'''


'''-------------------------------------------------------------'''



def pic_execute(pic_path):
    resu = detector.DetectPic(pic_path)
    item_name_list = AnalyzeResultsToItemsNamesList_pic(resu)
    for name in item_name_list:
        if check_event_pic(name):
            player.play_sound_pic(name)



def video_execute(video_path):
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
            if check_event_video(name,id):
                player.play_sound_video(name)

#下一步解决当下最大的问题：视频事件逻辑/time先后顺序/叫声重叠等如何解决？能不能给一个「引导方案」？

#文件夹里多个视频循环，每一个新视频都要重置一下track，防止污染
def videos_folder_execute(folder_path):
    VideoPathList = VideosInDir(folder_path)
    for video_path in VideoPathList:
        detector.ResetTrack()
        video_execute(video_path)





#main:
video_execute(yolo_source_video)
pic_execute(yolo_source_pic)

#两个bug：1.不显示可视化框  2.同一个动物重复触发bark（需要利用编号，同一个出现一次只叫一下）✅
#疑问：video文件夹输入多个视频可以吗🤔