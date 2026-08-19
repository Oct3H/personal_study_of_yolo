import time

last_event = {}
Appeared_NameID_List = []
AnimalEventList = []

#check bug Aug19
appeared_id = []

'''----------------重置器----------------'''

def ResetEvent_TwoList():
    Appeared_NameID_List.clear()
    AnimalEventList.clear()

'''---------------------------------------'''

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

def IfAppeared_NameID_InList(NAME_ID_TUPLE):
    if NAME_ID_TUPLE not in Appeared_NameID_List:
        return False
    else:
        return True



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
        Appeared_NameID_List.append((animal_name,id))#添加元组
        return True
    else:
        ExistEvent = FindAnimalEventInList(animal_name,id)#类似于指针，不是复制出一个新的对象，而是EE就是原本那个对象
        if now - ExistEvent.lasttime > 2:#这里逻辑重复了   实现：只叫一次，再出现不叫
            if IfAppeared_NameID_InList((animal_name,id)):            #预留接口： 隔2s去掉if可以再叫
                return False
            else:
                ExistEvent.update()
                return True
        else:
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






#bug check Aug19
def check_event_single_video(animal_name,id):
    now = time.time()
    if animal_name not in last_event:
        if id not in appeared_id:
            last_event[animal_name]=now
            appeared_id.append(id)
            return True
        else:
            return False
    else:
        if now - last_event[animal_name] > 2:
            if id not in appeared_id:
                appeared_id.append(id)
                return True
            else:
                return False
        else:
            return False