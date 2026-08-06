#   Analyze the object(results object) has how many pic->animal_object and store it
#into a LIST
#(analyze what in the pics/pic/frame

def AnalyzeResultsToItemsNamesList(A_Results):
    item_name_list =[]
    for pic in A_Results:
        for cls_number in pic.boxes.cls:#cls里的序号是「n.」，属于float；而names里的dict头是int，因此需要int化
            item_name = pic.names[int(cls_number)]
            item_name_list.append(item_name)
    return item_name_list

