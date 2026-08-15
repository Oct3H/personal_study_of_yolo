import time

last_event = {}
appeared_id = []
AnimalEventList = []

class AnimalEvent:
    def __init__(self,AnimalName,ID):
        self.name = AnimalName
        self.id = ID
        self.lasttime = time.time()#仅会在创建时更新一次，之后要靠函数更新
    def update(self):
        self.lasttime = time.time()


def FindAnimalEventInList(AnimalName,ID):
    for event in AnimalEventList:
        if event.name == AnimalName and event.id == ID:
            return event
    return None



#check event decide whether execute "play sound"
def check_event_pic(animal_name):
    now = time.time()
    if animal_name not in last_event:
        last_event[animal_name]=now
        return True
    else:
        if now - last_event[animal_name] > 2:
            return True
        else:
            return



def check_event_video(animal_name,id):
    now = time.time()
    if FindAnimalEventInList(animal_name,id)==None:
        NewOne = AnimalEvent(animal_name,id)
        AnimalEventList.append(NewOne)
        return True
    else:
        ExistEvent = FindAnimalEventInList(animal_name,id)#类似于指针，不是复制出一个新的对象，而是EE就是原本那个对象
        if now - ExistEvent.lasttime > 2:
            ExistEvent.update()
            return True
        else:
            ExistEvent.update()
            return False












'''----------------------------abandon code--------------------------------'''

# def check_event_video(animal_name,id):
#     now = time.time()
#     if animal_name not in last_event:
#         if id not in appeared_id:
#             last_event[animal_name]=now
#             appeared_id.append(id)
#             return True
#         else:
#             return False
#     else:
#         if now - last_event[animal_name] > 2:
#             if id not in appeared_id:
#                 appeared_id.append(id)
#                 return True
#             else:
#                 return False
#         else:
#             return False