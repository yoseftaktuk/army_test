from soldier1 import Soldier

class Residences:
    def __init__(self, number_room):
        self.number_room = number_room
        self.room = [] #list of personal number

    def add_soldier(self, soldier: Soldier):
        self.room.append(Soldier.get_personal_number())  
