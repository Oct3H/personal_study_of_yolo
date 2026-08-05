import detector,player
from config import yolo_source_pic,yolo_source_video
from detector import DetectFrame
from processor import video_process




#功能组合执行
#single pic/series of pics AND single frame ALL CAN use it to analyze animals and return bark
def analyze_and_return_bark(A_Results):
    for pic in A_Results:
        for cls_number in pic.boxes.cls:#cls里的序号是「n.」，属于float；而names里的dict头是int，因此需要int化
            item_name = pic.names[int(cls_number)]
            player.play_sound(item_name)



'''-------------------------------------------------------------'''


def pic_analyze(pic_path):
    resu = detector.DetectPic(pic_path)
    analyze_and_return_bark(resu)


def video_analyze(video_path):
    video_generator = video_process(video_path)
    frame_id = 0
    for Frame in video_generator:#迭代器内循环
        resu = DetectFrame(Frame)
        frame_id = frame_id + 1
        analyze_and_return_bark(resu)

#下一步解决当下最大的问题：视频事件逻辑/time先后顺序/叫声重叠等如何解决？能不能给一个「引导方案」？






#main: