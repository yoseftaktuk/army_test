class Room:
    def __init__(self,personal_number):
        self.space = []
        self.personal_number = personal_number
    def add_solder(self,solder):
        self.space.append(solder)    