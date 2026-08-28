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

        #防止没识别出id---没识别，直接跳过下面的小for，进入下一个大for循环
        if pic.boxes.id is None:
            continue

        for i in range(len(pic.boxes)):
            #利用字典保存ID name等多个信息--------nice method！！！✅
            obj = {
                "name": pic.names[int(pic.boxes.cls[i])],#cls里的序号是「n.」，属于float；而names里的dict头是int，因此需要int化
                "id"  : int(pic.boxes.id[i]),
                "conf": float(pic.boxes.conf[i])
            }
            item_name_id_DicList.append(obj)
    return item_name_id_DicList