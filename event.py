import time

last_event = {}

#check event decide whether execute "play sound"
def check_event(animal_name):
    now = time.time()
    if animal_name not in last_event:
        last_event[animal_name]=now
        return True
    else:
        if now - last_event[animal_name] > 2:
            return True
        else:
            return False

#下一步解决重复出现同一角色不重复bark