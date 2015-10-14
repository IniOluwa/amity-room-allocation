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


class Room(Space):
    def __init__(self, name):
        Space.__init__(self, name)
        self.limit = 4


class Amity(Room, Office):
    def __init__(self, name):
        Space.__init__(self, name)

    @staticmethod
    def place_people_in_spaces(spaces_available, type):
        file_read = PeopleFile().read_file()
        offices_allocation = file_read.get_fellows(
            ) if type == 'fellows' else file_read.get_staff()
        rooms_allocation = file_read.get_male_residential_fellows(
            ) if type == 'male_fellows' else file_read.get_female_residential_fellows()
        walker = 0
        if offices_allocation:
            for space in spaces_available:
                for num in range(len(offices_allocation)):
                    try:
                        space.add_person(offices_allocation[walker])
                    except:
                        continue
                    walker += 1
            return spaces_available

        elif rooms_allocation:
            for space in spaces_available:
                for num in range(len(rooms_allocation)):
                    try:
                        space.add_person(rooms_allocation[walker])
                    except:
                        continue
                    walker += 1
            return spaces_available
