#config可以被所有文件使用，但是其他文件尽量不要“函数交叉”
'''-------------------yolo----------------------'''
yolo_model = "yolo11n.pt"
yolo_source_pic = "images_/"
yolo_source_video = "videos_/duc.mp4"
yolo_source_VF = "videos_"






'''-------------------play----------------------'''

Animal = {
    "cat":{
        "sound_path":"sounds_/cat.mp3",
        "sound_content":"miao miao"
        },
    "dog":{
        "sound_path":"sounds_/dog.mp3",
        "sound_content":"woff woff"
        },
    "sheep":{
        "sound_path":"sounds_/sheep.mp3",
        "sound_content":"mei mei"
        },
    "elephant":{
        "sound_path":"sounds_/elephant.mp3",
        "sound_content":"muemmmmmmmmmm"
        }

}