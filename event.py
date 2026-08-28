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


    def Update(self,NAME,CONF):
        self.name = NAME
        if len(self.past_ten_frame)<50:
            self.past_ten_frame.append((NAME,CONF))
        else:
            del self.past_ten_frame[0]
            self.past_ten_frame.append((NAME,CONF))


    def TEN_FRAME_JUDGE(self):
        frist = self.past_ten_frame[0][0]
        last  = self.past_ten_frame[-1][0]

        score = {}

        for name, conf in self.past_ten_frame:
            if name not in score:
                score[name] = [0,0]#rate & times

            score[name][0] += conf
            score[name][1] += 1
        #按照平均值算最大的
        best_name = max(score, key=lambda name: score[name][0]/score[name][1])
        best_score = score[best_name][0]/score[best_name][1]

        if best_score<=0.5:
            return False
        else:
            if score[best_name][1]<len(self.past_ten_frame)/2:
                return False
            else:
                if best_name == last:
                    return True
                else:
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
def check_event_video(animal_name,id,conf):
    #None保护
    if animal_name is None or id is None:
        return False
    #现在时间
    now = time.time()

    #如果全新的跟踪---创建
    if FindAnimalEventInList(id) == None:
        NewOne = AnimalEvent(id)
        NewOne.Update(animal_name,conf)
        AnimalEventList.append(NewOne)
        Appeared_NameID_List.append((animal_name,id))#添加元组
        return True
    else:
        ExistEvent = FindAnimalEventInList(id)
        ExistEvent.Update(animal_name,conf)
        if ExistEvent.TEN_FRAME_JUDGE():
            if now - ExistEvent.lasttime > 2:#这里逻辑重复了   实现：只叫一次，再出现不叫
                        if IfAppeared_NameID_InList((animal_name,id)):            #预留接口： 隔2s去掉if可以再叫
                            return False
                        else:
                            ExistEvent.update_time()
                            return True
        else:
            return False