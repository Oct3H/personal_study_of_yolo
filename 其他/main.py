from ultralytics import YOLO
import pygame
pygame.mixer.init()#用pagame必须初始化（这里是因为只用mixer）⚠️⚠️⚠️
model = YOLO("yolo11n.pt")
#下面这俩是随便起的变量名（source&results）
source = "images_/"
results = model(source)#results：不是一个对象，而是一个list变量，里面储存着一个个对象，通过results[n]提取具体对象




'''--------------------------------------------------------------------------'''


'''实验1:'''
# print(type(results))
# print(results)
'''实验2:'''
# print(results[0])
# print("---------------------------------")
# print(results[0].boxes.numpy())
# print("---------------------------------")
# print(results[0].boxes.shape)
# print("---------------------------------")
# print(results[0].boxes.data)
# print("---------------------------------")
# print(results[0].boxes.id)


'''--------------------------------------------------------------------------------'''

CAT = 15
DOG = 16
BENCH = 13
SHEEP = 18
ELEP = 20


def play_cat_sound():
    cat_sound = pygame.mixer.Sound("sounds_/cat.mp3")
    cat_sound.play()#这个默认是同时播放⚠️
def play_dog_sound():
    dog_sound = pygame.mixer.Sound("sounds_/dog.mp3")
    dog_sound.play()
def play_sheep_sound():
    sheep_sound = pygame.mixer.Sound("sounds_/sheep.mp3")
    sheep_sound.play()
def play_elephant_sound():
    elephant_sound = pygame.mixer.Sound("sounds_/elephant.mp3")
    elephant_sound.play()



# for pic in results:
#     for item in pic.boxes.cls:
#         if item == CAT:
#             print('cat : miao')
#             play_cat_sound()
#         elif item == DOG:
#             print("dog : wowo")
#             play_dog_sound()
#         elif item == ELEP:
#             print("elephant : emwooo")
#             play_elephant_sound()
#         elif item == SHEEP:
#             print("sheep : meimei")
#             play_sheep_sound()
#         else:
#             print("This item isn`t life")
#         pygame.time.wait(1500)



import cv2
path = "*.mp4"
#返回一个generator类型参数Frames = ∑ frame
def video_get(Path):
    cap = cv2.VideoCapture(Path)
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        yield frame
    cap.release()

#每一帧都是一个图片识别,一个results里包含多个pic的识别结果??不对
def FrameProcess(frame):
    results = model(frame)
    return results

def DetectFrame(results):
    for pic in results:
        for item in pic.boxes.cls:
            if item == CAT:
                print('cat : miao')
                play_cat_sound()
            elif item == DOG:
                print("dog : wowo")
                play_dog_sound()
            elif item == ELEP:
                print("elephant : emwooo")
                play_elephant_sound()
            elif item == SHEEP:
                print("sheep : meimei")
                play_sheep_sound()
            else:
                print("This item isn`t life")


video_generator = video_get(path)
frame_id = 0
for frame in video_generator:
    frame_id=frame_id+1
    resu = FrameProcess(frame)
    DetectFrame(resu)








