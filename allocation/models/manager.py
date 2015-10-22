"""
Manager class that creates instances of offices and room spaces,
then allocates people to them.
"""
from spaces import OfficeSpace, LivingSpace
from fileparser import FileParser


class Manager(object):
    def __init__(self):
        self.spaces_available = []

    def space_placing(self):
        """Automatic creation OfficeSpace and LivingSpace instances"""
        spaces = open('data\spaces.txt')
        for line in iter(spaces):
            line = line.split()
            space_type = line[1]
            name = line[0]
            occupant_type = line[2]
            if space_type == 'OFFICE':
                space = OfficeSpace(name, space_type, occupant_type)
                self.spaces_available.append(space)
            elif space_type == 'ROOM':
                space = LivingSpace(name, space_type, occupant_type)
                self.spaces_available.append(space)

    def list_spaces(self):
        """List of spaces_available"""
        return self.spaces_available

    def allocation(self):
        """Sorting out of spaces occupants"""
        people = FileParser().read_file()
        staff = people.get_staff()
        fellows = people.get_fellows()
        males = people.get_male_residential_fellows()
        females = people.get_female_residential_fellows()

        for space in self.spaces_available:
            try:
                for person in staff:
                    # allocate each person to an office
                    if space.space_type == 'OFFICE':
                        space.add_person(person)
                        staff.remove(person)

                for person in fellows:
                    # allocate each person to an office
                    if space.space_type == 'OFFICE':
                        space.add_person(person)
                        fellows.remove(person)

                for person in males:
                    # allocate each person to a male living space
                    if space.occupant_type == 'MALE':
                        space.add_person(person)
                        males.remove(person)

                for person in females:
                    # allocate each person to a female living space
                    if space.occupant_type == 'FEMALE':
                        space.add_person(person)
                        females.remove(person)
            except:
                    continue

    def unallocated_fellows(self):
        """All unallocated fellows"""
        people = FileParser().read_file()
        unallocated = people.get_unallocated_fellows()
        print unallocated
