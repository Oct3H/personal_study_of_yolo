import cv2

#视频一帧里只有一个图-->results里只有一个results[0]
#这一个图里可以有多个物体，因此可以有很多框（box）
#!!框是在原始帧上的，不在results上，因此必须有帧传入

def show_box(frame,results):#利用「双传参」引入frame图片变量
    #修改图片(图片加框)
    boxes = results[0].boxes
    names = results[0].names

    # Tracking ID 可能为 None
    if boxes.id is not None:

        for i in range(len(boxes)):
            # box
            x1, y1, x2, y2 = boxes.xyxy[i]

            # class
            class_id = int(boxes.cls[i])
            name = names[class_id]

            # tracking ID
            track_id = int(boxes.id[i])

            # confidence
            conf = float(boxes.conf[i])

            # 画框
            cv2.rectangle(
                frame,
                (int(x1), int(y1)),
                (int(x2), int(y2)),
                (0, 255, 0),
                2
            )

            # 显示文字
            label = f"{name} ID:{track_id} conf:{conf:.2f}"

            cv2.putText(
                frame,
                label,
                (int(x1), int(y1) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # 告诉「窗口」，要显示(这个被修改后的)图片
    cv2.imshow(
        "video",#窗口名称
        frame   #图片变量
    )

    #创建窗口并设置刷新速度
    #停留约1毫秒，让窗口刷新，然后继续下一帧
    cv2.waitKey(1)