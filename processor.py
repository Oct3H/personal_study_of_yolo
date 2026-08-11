import cv2,os
'''-------Read input and Process it to one by one Frame-------'''

#process the video to many frame(into a Generator)
#返回一个generator类型参数Frames = ∑ frame
def video_process(Path):
    cap = cv2.VideoCapture(Path)
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        yield frame
    cap.release()


#解决文件夹多个视频文件，用list存储各个视频路径(str)
def VideosInDir(folder):
    VideoPathList = []
    for filename in os.listdir(folder):
        if filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
            video_path = os.path.join(folder,filename)
            VideoPathList.append(video_path)
    return VideoPathList