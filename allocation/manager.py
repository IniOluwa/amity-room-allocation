
from spaces import Space, OfficeSpace, LivingSpace
from inputting import PeopleFile


class Manager(object):
    def __init__(self):
        self.spaces_available = []
        self.space_type = None
        self.occupant_type = None

    def space_placing(self):
        spaces = open('spaces.txt')
        for line in iter(spaces):
            line = line.split()
            name = line[0]
            self.space_type = line[1]
            space = name.lower()
            self.occupant_type = line[2]
            if self.space_type == 'OFFICE':
                space = OfficeSpace(name, self.space_type, self.occupant_type)
                self.spaces_available.append(space)
            elif self.space_type == 'ROOM':
                space = LivingSpace(name, self.space_type, self.occupant_type)
                self.spaces_available.append(space)

    def list_spaces(self):
        return self.spaces_available

    def staff_allocation(self):
        people = PeopleFile().read_file()
        staffs = people.get_staff()
        walker = 0
        for space in self.spaces_available:
            if space.occupant_type == 'STAFF':
                for staff in range(len(staffs)):
                    try:
                        space.add_person(staffs[walker])
                    except:
                        continue
                    walker = walker + 1

    def get_staff_placement(self):
        return [space for space in self.spaces_available if space.occupant_type == 'STAFF']

    def fellow_allocation(self):
        people = PeopleFile().read_file()
        fellows = people.get_fellows()
        walker = 0
        for space in self.spaces_available:
            if space.occupant_type == 'FELLOW':
                for fellow in range(len(fellows)):
                    try:
                        space.add_person(fellows[walker])
                    except:
                        continue
                    walker = walker + 1

    def get_fellow_placement(self):
        return [space for space in self.spaces_available if space.occupant_type == 'FELLOW']

    def male_allocation(self):
        people = PeopleFile().read_file()
        males = people.get_male_residential_fellows()
        walker = 0
        for space in self.spaces_available:
            if space.occupant_type == 'MALE':
                for male in range(len(males)):
                    try:
                        space.add_person(males[walker])
                    except:
                        continue
                    walker = walker + 1

    def get_male_placement(self):
        return [space for space in self.spaces_available if space.occupant_type == 'MALE']

    def female_allocation(self):
        people = PeopleFile().read_file()
        females = people.get_female_residential_fellows()
        walker = 0
        for space in self.spaces_available:
            if space.occupant_type == 'FEMALE':
                for female in range(len(females)):
                    try:
                        space.add_person(females[walker])
                    except:
                        continue
                    walker = walker + 1

    def get_female_placement(self):
        return [space for space in self.spaces_available if space.occupant_type == 'FEMALE']