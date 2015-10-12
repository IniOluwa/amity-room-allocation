from allocation_people_input_class import PeopleFile
from allocation_spaces import Room


class FemaleRooms:
    def __init__(self):
        iroko = Room('Iroko')
        obeche = Room('obeche')
        juniper = Room('Juniper')
        aishte = Room('Aishte')
        self.rooms_available = [iroko, obeche, juniper, aishte]

    def place_female_fellows_in_rooms(self):
        return Room.place_fellows_in_rooms(self.rooms_available, 'female_fellows')

    def number_of_rooms(self):
        return len(self.rooms_available)
