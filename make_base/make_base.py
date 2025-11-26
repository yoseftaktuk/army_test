from residences.residences import Residences 
from base.base import Base
from soldier1.soldier import Soldier
from server.file_endler.file_endler1 import load_data, seve_data
from make_base.valid1 import check_pesonal_num, check_room

def make_soldier():
    soldiers_to_register = []
    data = load_data()
    for ditels in data:
        if check_pesonal_num(ditels[0]):
            sobgect_soldier = Soldier(personal_number=int(ditels[0]), firs_name=ditels[1],last_name=ditels[2],
                                sex=ditels[3],city_of_residence=ditels[4], distance_base=ditels[5],placement_mode='Not_assigned')
            soldiers_to_register.append(sobgect_soldier)
        else:
            continue          
    return soldiers_to_register

def sort_soldier(soldier_list: list):
   n = len(soldier_list)
   for i in range(n-1):
        for j in range(n-i-1):
            if int(soldier_list[j].distance_base) > int(soldier_list[j+1].distance_base):
                soldier_list[j], soldier_list[j+1] = soldier_list[j+1], soldier_list[j]
   return soldier_list             


def make_residences(num_residences):
    residences_list = []
    for i in range(num_residences):
        residences = Residences(number_room=10,personal_number=i+1)
        residences_list.append(residences)
    print(len(residences_list))    
    return residences_list


def soldier_registration_to_room(residences_list: list,soldiers_to_register : list):
    soldier_assigned = []
    soldiers_not_register = []
    for residences in residences_list:
        for room in residences.rooms:    
            while check_room(len(room.space)):
                if len(soldiers_to_register) > 0:
                    soldier = soldiers_to_register.pop()
                    soldier.placement_mode = 'assigned'
                    soldier.room_number = room.personal_number
                    room.add_solder(soldier)
                    soldier_assigned.append(soldier)        
                else:
                    break    
    if soldiers_to_register:
        for solider1 in soldiers_to_register:
            soldiers_not_register.append(solider1)     
    data = {'soldier_assigned': soldier_assigned,
            'soldiers_not_register': soldiers_not_register}
    #seve_data(data=data)  
    return residences_list, soldiers_not_register,soldiers_not_register
  


def placement(num_residences):
    soldiers_to_register =  make_soldier()
    order_solder_list = sort_soldier(soldier_list=soldiers_to_register)
    residences = make_residences(num_residences)
    residences_list = soldier_registration_to_room(residences_list=residences, 
                                        soldiers_to_register=order_solder_list)
    return residences_list

def make_base(num_residences): 
    residences_list = placement(num_residences)   
    base = Base()
    for r in residences_list[0]:
        base.add_residences(r)
    soldiers_not_register =  residences_list[1]  
    soldiers_register = residences_list[2]
    residences_list1 = residences_list[0]
    print(soldiers_register)
    return base, soldiers_register, soldiers_not_register, residences_list1 



    


    

