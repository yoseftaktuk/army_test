from residences import residences


class Base:
    def __init__(self):
        self.base = {}

    def add_residences(self, residences:residences.Residences ):
        self.base[residences.number_room] = residences
        
