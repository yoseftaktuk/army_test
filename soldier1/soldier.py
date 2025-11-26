

class Soldier:
    def __init__(self,personal_number,firs_name ,last_name,sex, city_of_residence, distance_base, placement_mode):
        self._personal_number = personal_number
        self.firs_name = firs_name
        self.last_name = last_name
        self.sex = sex
        self.city_of_residence = city_of_residence
        self.distance_base = distance_base
        self.placement_mode = placement_mode
    def get_personal_number(self):
        return self._personal_number

    