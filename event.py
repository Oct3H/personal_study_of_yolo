import time
from collections import Counter

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
    def __init__(self,ID):
        self.id = ID
        self.lasttime = time.time()#仅会在创建时更新一次，之后要靠函数更新
        self.past_ten_frame = []
        self.name = ''

    def update_time(self):
        self.lasttime = time.time()


    def update_name(self,NAME):
        self.name = NAME
        if len(self.past_ten_frame)<100:
            self.past_ten_frame.append(NAME)
        else:
            del self.past_ten_frame[0]
            self.past_ten_frame.append(NAME)


    def TEN_FRAME_JUDGE(self):
        first = self.past_ten_frame[0]
        last = self.past_ten_frame[-1]

        counter = Counter(self.past_ten_frame)
        most_name, most_count = counter.most_common(1)[0]

        half = len(self.past_ten_frame) / 2

        # 当前类别已经成为多数
        if most_name == last and most_count >= half:
            return True

        return False





def FindAnimalEventInList(ID):
    for event in AnimalEventList:
        if event.id == ID:
            return event
    return None

def IfAppeared_NameID_InList(NAME_ID_TUPLE):
    if NAME_ID_TUPLE not in Appeared_NameID_List:
        return False
    else:
        return True


'''-------'''

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







#🆔为核心的重新设计：
def check_event_video(animal_name,id):
    #None保护
    if animal_name is None or id is None:
        return False
    #现在时间
    now = time.time()

    #如果全新的跟踪---创建
    if FindAnimalEventInList(id) == None:
        NewOne = AnimalEvent(id)
        NewOne.update_name(animal_name)
        AnimalEventList.append(NewOne)
        Appeared_NameID_List.append((animal_name,id))#添加元组
        return True
    else:
        ExistEvent = FindAnimalEventInList(id)
        ExistEvent.update_name(animal_name)
        if ExistEvent.TEN_FRAME_JUDGE():
            if now - ExistEvent.lasttime > 2:#这里逻辑重复了   实现：只叫一次，再出现不叫
                        if IfAppeared_NameID_InList((animal_name,id)):            #预留接口： 隔2s去掉if可以再叫
                            return False
                        else:
                            ExistEvent.update_time()
                            return True
        else:
            return False













'''------------------10帧判定--------------------------'''







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



#老class
# def __init__(self,AnimalName,ID):
#     self.name = AnimalName
#     self.id = ID
#     self.lasttime = time.time()#仅会在创建时更新一次，之后要靠函数更新
#     self.past_ten_frame = []

# def TEN_FRAME_JUDGE(self):
#     frist = self.past_ten_frame[0]
#     last = self.past_ten_frame[len(self.past_ten_frame) - 1]
#
#     half_of_list = len(self.past_ten_frame) / 2
#     quarter_of_list = len(self.past_ten_frame) / 4
#
#     counter = Counter(self.past_ten_frame)
#     items_appear_times = counter.most_common()  # mostcommon返回是list形式
#     if items_appear_times[0][0] == frist and items_appear_times[0][1] >= half_of_list:
#         return False
#     elif frist == last and items_appear_times[0][1] >= quarter_of_list:
#         return False
#     # 最新加的出现最多次数
#     elif items_appear_times[0][0] == last and items_appear_times[0][1] >= half_of_list:
#         return True
#     else:
#         return False




# def check_event_video(animal_name,id):
#
#     #None保护
#     if animal_name is None or id is None:
#         return False
#
#     now = time.time()
#     if FindAnimalEventInList(animal_name,id)==None:
#         NewOne = AnimalEvent(animal_name,id)
#         AnimalEventList.append(NewOne)
#         Appeared_NameID_List.append((animal_name,id))#添加元组
#         return True
#     else:
#         ExistEvent = FindAnimalEventInList(animal_name,id)#类似于指针，不是复制出一个新的对象，而是EE就是原本那个对象
#         if now - ExistEvent.lasttime > 2:#这里逻辑重复了   实现：只叫一次，再出现不叫
#             if IfAppeared_NameID_InList((animal_name,id)):            #预留接口： 隔2s去掉if可以再叫
#                 return False
#             else:
#                 ExistEvent.update()
#                 return True
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