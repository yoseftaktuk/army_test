
def check_pesonal_num(num):
    try:
        if int(num) // 1000000 == 8:
            return True
    except TypeError:    
        return False

def check_room(num):
    if num == 8:
        return False
    return True

