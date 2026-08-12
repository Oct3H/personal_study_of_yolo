import time

last_event = {}
appeared_id = []


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

