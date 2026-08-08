import detector,player
from analyzer import AnalyzeResultsToItemsNamesList
from config import yolo_source_pic,yolo_source_video
from detector import DetectFrame
from event import check_event
from processor import video_process
from visualizer import show_case

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
    item_name_list = AnalyzeResultsToItemsNamesList(resu)
    for name in item_name_list:
        if check_event(name):
            player.play_sound(name)


def video_execute(video_path):
    video_generator = video_process(video_path)
    frame_id = 0
    #every frame：
    # 视频一帧里只有一个图-->results里只有一个results[0]
    for Frame in video_generator:#迭代器内循环
        resu = DetectFrame(Frame)
        frame_id = frame_id + 1
        show_case(Frame,resu)
        item_name_list = AnalyzeResultsToItemsNamesList(resu)
        for name in item_name_list:
            if check_event(name):
                player.play_sound(name)

#下一步解决当下最大的问题：视频事件逻辑/time先后顺序/叫声重叠等如何解决？能不能给一个「引导方案」？






#main:
video_execute(yolo_source_video)

#两个bug：1.不显示可视化框  2.同一个动物重复触发bark（需要利用编号，同一个出现一次只叫一下）