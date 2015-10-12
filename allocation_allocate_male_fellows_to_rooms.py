from allocation_people_input_class import PeopleFile
from allocation_spaces import Room


class MaleRooms:
    def __init__(self):
        olive = Room('Olive')
        tongs = Room('Tongs')
        mahogany = Room('Mahogany')
        sapele = Room('Sapele')
        maple = Room('Maple')
        konoha = Room('Konoha')
        self.rooms_available = [olive, tongs, mahogany, sapele, maple, konoha]

    def place_male_fellows_in_rooms(self):
        return Room.place_male_fellows_in_rooms

    def number_of_rooms(self):
        return len(self.rooms_available)
