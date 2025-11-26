from residences.residences import Residences 
from base.base import Base
from soldier1.soldier import Soldier
from server.file_endler.file_endler1 import load_data
import valid

def make_soldier():
    soldiers_to_register = []
    data = load_data()
    for ditels in data:
        if valid.check_pesonal_num(ditels[0]):
            sobgect_soldier = Soldier(personal_number=int(ditels[0]), firs_name=ditels[1],last_name=ditels[2],
                                sex=ditels[3],city_of_residence=ditels[4], distance_base=ditels[5])
            soldiers_to_register.append(sobgect_soldier)
    return soldiers_to_register

def make_residences(num_residences):
    residences_list = []
    for i in range(num_residences - 1):
        residences = Residences(10)
        residences_list.append(residences)
    return residences_list


def soldier_registration(residences_list: list,soldiers_to_register : list):
    for residences in residences_list:
        while valid.check_room(len(residences.room)):
            residences.add_soldier(soldiers_to_register.pop())

def base(num_residences):
    soldiers_to_register =  make_soldier()
    residences = make_residences(num_residences)
    registration = soldier_registration(residences_list=residences, 
                                        soldiers_to_register=soldier_registration)
    return registration





    


