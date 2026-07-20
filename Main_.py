import detector,player
from config import yolo_source

results = detector.detector_source(yolo_source)
for pic in results:
    for cls_number in pic.boxes.cls:#cls里的序号是「n.」，属于float；而names里的dict头是int，因此需要int化
        item_name = pic.names[int(cls_number)]
        player.play_sound(item_name)