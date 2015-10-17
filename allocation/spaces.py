class Space:
    def __init__(self, name, type, occupant_type):
        self.spaces = open('spaces.txt')
        self.people = []
        for line in iter(self.spaces):
            self.name = line[0]
            self.space_name = self.name.lower()
            self.type = line[1]
            self.occupant_type = line[2]
            if self.type == 'OFFICE':
                self.space_name = OfficeSpace(self.name)
            elif self.type == 'ROOM':
                self.space_name = LivingSpace(self.name)

    def add_person(self, person):
        if self.limit != 0:
            self.people.append(person)
            self.limit-1
        else:
            raise Exception("We are out of spaces.")

    def __repr__(self):
        return "%s" % self.name


class OfficeSpace(Space):
    def __init__(self):
        self.limit = 6


class LivingSpace(Space):
    def __init__(self):
        self.limit = 4
