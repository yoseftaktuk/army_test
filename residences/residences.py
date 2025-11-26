from soldier1 import soldier
from room.room import Room

def make_10_room():
    list_room = []
    for i in range(9):
        room_1 = Room(i + 1)
        list_room.append(room_1)
    return list_room    

class Residences:
    def __init__(self, number_room, personal_number):
        self.number_rooms = number_room
        self.rooms = make_10_room() 
        self.personal_number = personal_number

    def add_room(self,room):
        self.rooms.append(room)  
