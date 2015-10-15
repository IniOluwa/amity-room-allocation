from inputting import PeopleFile


class Space:
    """Single office instantiation class"""
    def __init__(self, name):
        self.name = name
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


class Office(Space):
    def __init__(self, name):
        Space.__init__(self, name)
        self.limit = 6

    @staticmethod
    def place_people_in_offices(offices_available, type):
        """method for placing people in offices"""
        file_read = PeopleFile().read_file()
        people_list = file_read.get_fellows() if type=='fellows' else file_read.get_staff()
        office_walker = 0
        for office in offices_available:
            for num in range(len(people_list)):
                try:
                    office.add_person(people_list[office_walker])
                except:
                    continue
                office_walker += 1
        return offices_available



class Room(Space):
    def __init__(self, name):
        Space.__init__(self, name)
        self.limit = 4

    @staticmethod
    def place_fellows_in_rooms(rooms_available, type):
        """method for placing people in rooms"""
        file_read = PeopleFile().read_file()
        people_list = file_read.get_male_residential_fellows() if type=='male_fellows' else file_read.get_female_residential_fellows()
        room_walker = 0
        for room in rooms_available:
            for num in range(len(people_list)):
                try:
                    room.add_person(people_list[room_walker])
                except:
                    continue
                room_walker += 1
        return rooms_available
