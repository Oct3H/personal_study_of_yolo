import cv2
'''-------Read input and  Process it to one by one Frame-------'''

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
