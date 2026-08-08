import cv2

#视频一帧里只有一个图-->results里只有一个results[0]
#这一个图里可以有多个物体，因此可以有很多框（box）
#!!框是在原始帧上的，不在results上，因此必须有帧传入

def show_case(frame,results):#利用「双传参」引入frame图片变量
    #修改图片(图片加框)
    for box in results[0].boxes.xyxy:
        x1,y1,x2,y2 = box
        cv2.rectangle(
            frame,#图片变量
            (int(x1),int(y1)),
            (int(x2),int(y2)),
            (0,255,0),#colour
            2#线宽
        )

    #打开窗口，显示图片
    cv2.imshow(
        "video",
        frame   #图片变量
    )