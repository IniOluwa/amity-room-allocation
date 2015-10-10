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
        male_fellows_list = PeopleFile().read_file().get_male_residential_fellows()
        room_walker = 0
        for room in self.rooms_available:
            for num in range(len(male_fellows_list)):
                try:
                    room.add_person(male_fellows_list[room_walker])
                except:
                    continue
                room_walker += 1
        return self.rooms_available

    def number_of_rooms(self):
        return len(self.rooms_available)
