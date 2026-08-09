#   Analyze the object(results object) has how many pic->animal_object and store it
#into a LIST
#(analyze what in the pics/pic/frame

def AnalyzeResultsToItemsNamesList_pic(A_Results):
    item_name_list =[]
    for pic in A_Results:
        for cls_number in pic.boxes.cls:#cls里的序号是「n.」，属于float；而names里的dict头是int，因此需要int化
            item_name = pic.names[int(cls_number)]
            item_name_list.append(item_name)
    return item_name_list

def AnalyzeResultsToItemsNamesList_video(A_Results):
    item_name_id_DicList =[]
    for pic in A_Results:#results出自model.track的话，boxes里多加了id
        for i in range(len(pic.boxes)):
            #利用字典保存ID name等多个信息--------nice method！！！✅
            obj = {
                "name": pic.names[int(pic.boxes.cls[i])],#cls里的序号是「n.」，属于float；而names里的dict头是int，因此需要int化
                "id"  : pic.boxes.id[i]
            }
            item_name_id_DicList.append(obj)
    return item_name_id_DicList






'''
            boxes
             |
             ├── xyxy
             │     [
             │       box0坐标,
             │       box1坐标,
             │       box2坐标
             │     ]
             │
             ├── cls
             │     [
             │       box0类别,
             │       box1类别,
             │       box2类别
             │     ]
             │
             ├── conf
             │     [
             │       box0置信度,
             │       box1置信度,
             │       box2置信度
             │     ]
             │
             └── id
                   [
                     box0 ID,
                     box1 ID,
                     box2 ID
                   ]
'''