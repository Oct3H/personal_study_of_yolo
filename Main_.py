import detector,player
import event
from analyzer import AnalyzeResultsToItemsNamesList_pic,AnalyzeResultsToItemsNamesList_video
from config import yolo_source_pic,yolo_source_video,yolo_source_VF
from detector import DetectFrame, DetectSingleVideoFrame
from event import check_event_pic, check_event_video, check_event_single_video
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











#bug check Aug19
def Single_video_execute(video_path):
    video_generator = video_process(video_path)
    frame_id = 0#暂时没啥用。。。
    #every frame：
    # 视频一帧里只有一个图-->results里只有一个results[0]
    for Frame in video_generator:#迭代器内循环
        resu = DetectSingleVideoFrame(Frame)#wtf这里没换成detectsinglevideoframe😱，就是event的问题---->换成了，没有识别出🐑了，就是.track模式下模型的问题😅
        '''resu = DetectFrame(Frame)'''#换之前1️⃣
        frame_id = frame_id + 1
        # show_box(Frame,resu)
        # item_NameID_list = AnalyzeResultsToItemsNamesList_video(resu)
        # for obj in item_NameID_list:
        #     name = obj["name"]
        #     id = obj["id"]
        #     if check_event_single_video(name,id):
        #         player.play_sound_video(name)
        for result in resu:
            for i in range(len(result.boxes)):
                print(
                    "frame:", frame_id,
                    "name:", result.names[int(result.boxes.cls[i])],
                    # "id:", int(result.boxes.id[i]),           #换之前1️⃣
                    # "conf:", float(result.boxes.conf[i])      #换之前1️⃣
                )#-----发现异常所在：模型问题😂，把16、17帧的狗识别为羊，并赋予id=1，因此老版本（只看id复现）没bug，新版本（name+id双保证）不行了
                    #此时🐑的识别率约0.3，但是大于🐶，因此当作羊了





'''----------------------------main---------------------------------'''

#main:
#video_execute(yolo_source_video)
#pic_execute(yolo_source_pic)
videos_folder_execute(yolo_source_VF)



#check bug Aug19
#Single_video_execute(yolo_source_video)





#Question & Bug & Next Step
#✅下一步解决当下最大的问题：视频事件逻辑/time先后顺序/叫声重叠等如何解决？能不能给一个「引导方案」？
#✅两个bug：1.不显示可视化框  2.同一个动物重复触发bark（需要利用编号，同一个出现一次只叫一下）✅
#✅疑问：video文件夹输入多个视频可以吗🤔
#✅bug： 1.track id没分配导致id返回值为None  2.在event里设计「10 帧投票 + conf比较」
#下一步加上conf比较，和「10帧投票」结合😠


#⚠️id是给“被追踪实例”的编号，并非"新的事物第一次出现就是id=1"(ID 通常不会因为类别不同而重新从 1 开始)
# 如果追踪实例由🐶莫名变成🐯，id也会继承（类似变形金钢，🚗变人）



'''-------------------------------------------------------------'''


'''
#功能组合执行(早已废弃⚠️)
#single pic/series of pics AND single frame ALL CAN use it to analyze animals and return bark
def analyze_and_return_bark(A_Results):
    for pic in A_Results:
        for cls_number in pic.boxes.cls:#cls里的序号是「n.」，属于float；而names里的dict头是int，因此需要int化
            item_name = pic.names[int(cls_number)]
            player.play_sound(item_name)
'''


'''-------------------------------------------------------------'''
