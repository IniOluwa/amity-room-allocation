
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

    def allocate(self):
        people = PeopleFile().read_file()
        staffs = people.get_staff()
        fellows = people.get_fellows()
        males = people.get_male_residential_fellows()
        females = people.get_female_residential_fellows()
        unallocated = people.get_unallocated_fellows()
        walker = 0
        for space in self.spaces_available:
            if space.occupant_type == 'STAFF':
                people_list = staffs
            elif space.occupant_type == 'FELLOW':
                people_list = fellows
            elif space.occupant_type == 'MALE':
                people_list = males
            elif space.occupant_type == 'FEMALE':
                people_list = females
            else:
                people_list = unallocated

            for person in range(len(people_list)):
                try:
                    space.add_person(people_list[walker])
                except:
                    continue
                walker = walker + 1
