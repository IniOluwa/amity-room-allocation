"""
Manager class that creates instances of offices and room spaces,
then allocates people to them.
"""
from spaces import OfficeSpace, LivingSpace
from fileparser import FileParser
import os


class Manager(object):
    """
    The manager object has methods for allocating people to spaces.
    """
    def __init__(self):
        self.spaces_available = []
        self.people = FileParser().read_file()
        self.staff = self.people.get_staff()
        self.fellows = self.people.get_fellows()
        self.males = self.people.get_male_residential_fellows()
        self.females = self.people.get_female_residential_fellows()
        self.unallocated_staff = []
        self.unallocated_fellows_to_officespaces = []
        self.unallocated_fellows_to_livingspaces = []

    def space_placing(self):
        """Create OfficeSpace and LivingSpace instances"""
        spaces = open(os.path.join('data', 'spaces.txt'))
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

    def generate_spaces(self):
        """Generate spaces that are not filled"""
        for space in self.spaces_available:
            if not space.is_filled():
                yield space
            else:
                yield space.next()

    def list_spaces(self):
        """List of spaces_available"""
        return self.spaces_available

    def allocation(self):
        """Sorting out of spaces occupants"""

        for space in self.generate_spaces():
            try:
                # allocate each staff to an office
                if space.occupant_type == 'STAFF':
                    for person in self.staff:
                        space.add_person(person)

                # allocate each fellow to an office
                if space.occupant_type == 'FELLOW':
                    for person in self.fellows:
                        space.add_person(person)

                # allocate each male-fellow to a male living space
                if space.occupant_type == 'MALE':
                    for person in self.males:
                        space.add_person(person)

                # allocate each female-fellow to a female living space
                if space.occupant_type == 'FEMALE':
                    for person in self.females:
                        space.add_person(person)
            except:
                    continue

        """Return unallocated people after allocation"""
        for person in self.people:
            if person.role == 'STAFF':
                if not person.has_officespace:
                    self.unallocated_staff.append(person)
            elif person.role == 'FELLOW':
                if not person.has_officespace:
                    self.unallocated_fellows_to_officespaces.append(person)
                if not person.has_livingspace:
                    self.unallocated_fellows_to_livingspaces.append(person)
