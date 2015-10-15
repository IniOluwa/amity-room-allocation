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


class Amity(Space):
    def __init__(self, name):
        Space.__init__(self, name)

    @staticmethod
    def space(spaces_available, type):
        file_read = PeopleFile().read_file()
        walker = 0
        offices_allocation = file_read.get_fellows(
            ) if type == 'fellows' else file_read.get_staff()

        if offices_allocation:
            for space in spaces_available:
                if type == 'fellows':
                    for num in range(len(offices_allocation)):
                        try:
                            space.add_person(offices_allocation[walker])
                        except:
                            continue
                        walker += 1
                else:
                    for num in range(len(offices_allocation)):
                        try:
                            space.add_person(offices_allocation[walker])
                        except:
                            continue
                        walker += 1
            return spaces_available
        # elif rooms_allocation:
        #     for space in spaces_available:
        #         if type == 'male_fellows':
        #             for num in range(len(rooms_allocation)):
        #                 try:
        #                     space.add_person(rooms_allocation[walker])
        #                 except:
        #                     continue
        #                 walker += 1
        #         else:
        #             for num in range(len(rooms_allocation)):
        #                 try:
        #                     space.add_person(rooms_allocation[walker])
        #                 except:
        #                     continue
        #                 walker += 1
        #     room_spaces = spaces_available
        #     return room_spaces

    @staticmethod
    def sp(spaces_available, type):
        file_read = PeopleFile().read_file()
        walker = 0
        rooms_allocation = file_read.get_male_residential_fellows(
        ) if type == 'male_fellows' else file_read.get_female_residential_fellows()
        if rooms_allocation:
            for space in spaces_available:
                if type == 'male_fellows':
                    for num in range(len(rooms_allocation)):
                        try:
                            space.add_person(rooms_allocation[walker])
                        except:
                            continue
                        walker += 1
                else:
                    for num in range(len(rooms_allocation)):
                        try:
                            space.add_person(rooms_allocation[walker])
                        except:
                            continue
                        walker += 1
            return spaces_available
