from allocation_people_input_class import PeopleFile


class Room:
    def __init__(self, name):
        self.name = name
        self.limit = 4
        self.people = []

    def add_person(self, person):
        if self.limit != 0:
            self.people.append(person)
            self.limit -= 1
        else:
            raise Exception('We are out of office spaces')

    def list_persons(self):
        return self.people

    def __repr__(self):
        return self.name


class FemaleRooms:
    def __init__(self):
        iroko = Room('Iroko')
        obeche = Room('obeche')
        juniper = Room('Juniper')
        aishte = Room('Aishte')
        self.rooms_available = [iroko, obeche, juniper, aishte]

    def place_female_fellows_in_rooms(self):
        female_fellows_list = PeopleFile().read_file().get_female_residential_fellows()
        room_walker = 0
        for room in self.rooms_available:
            for num in range(len(female_fellows_list)):
                try:
                    room.add_person(female_fellows_list[room_walker])
                except:
                    continue
                room_walker += 1
        return self.rooms_available

    def number_of_rooms(self):
        return len(self.rooms_available)
