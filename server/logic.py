def get_info(data: tuple):
    number_registered_soldiers = len(data[1])
    number_not_registered_soldiers = len(data[2])
    return number_registered_soldiers ,number_not_registered_soldiers

def checking_every_soldier(data):
    info = {}
    for solider in data[2]:
        print(solider)
        info[solider.get_personal_number()] = 'assigned', 'room number:'
        
    for solider in data[1]:   
        info[solider.get_personal_number()] = 'not assigned'
    return info    

