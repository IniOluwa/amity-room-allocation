"""
The Space class from which the OfficeSpace, and LivingSpace classes inherits from
This class is the core of all spaces created in the program.
"""


class Space:
    def __init__(self, name, space_type, occupant_type):
        self.name = name
        self.occupant_type = occupant_type
        self.space_type = space_type
        self.limit = None
        self.people = []

    def add_person(self, person):
        if len(self.people) < self.limit:
            self.people.append(person)
            if isinstance(self, OfficeSpace):
                person.has_officespace = True
            elif isinstance(self, LivingSpace):
                person.has_livingspace = True
            self.limit-1
        else:
            raise Exception("We are out of spaces.")

    def list_people(self):
        return self.people

    def __repr__(self):
        return "{}".format(self.name)


class OfficeSpace(Space):
    """OfficeSpace class which inherits from Space"""
    def __init__(self, name, space_type, occupant_type):
        Space.__init__(self, name, space_type, occupant_type)
        self.limit = 6

    def __repr__(self):
        return "{}".format(self.name)


class LivingSpace(Space):
    """LivingSpace class which inherits from Space"""
    def __init__(self, name, space_type, occupant_type):
        Space.__init__(self, name, space_type, occupant_type)
        self.limit = 4

    def __repr__(self):
        return "{}".format(self.name)
