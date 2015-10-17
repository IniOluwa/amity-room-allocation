from inputting import PeopleFile


class Space:
    def __init__(self, name, type, occupant_type):
        self.spaces = open('spaces.txt')
        self.spaces_available = []
        self.people = []
        for line in iter(self.spaces):
            self.name = line[0]
            self.space_name = self.name.lower()
            self.type = line[1]
            self.occupant_type = line[2]
            if self.type == 'OFFICE':
                self.space_name = OfficeSpace(self.name)
                self.spaces_available.append(self.space_name)
            elif self.type == 'ROOM':
                self.space_name = LivingSpace(self.name)
                self.spaces_available.append(self.space_name)

    def add_person(self, person):
        if self.limit != 0:
            self.people.append(person)
            self.limit-1
        else:
            raise Exception("We are out of spaces.")

    def list_spaces(self):
        return self.spaces_available

    def list_people(self):
        return self.people

    def __repr__(self):
        return "{}".format(self.name)


class OfficeSpace(Space):
    def __init__(self, name, space_type, occupant_type):
        Space.__init__(self, name, space_type, occupant_type)
        self.limit = 6
        people = PeopleFile().read_file()
        staffs = people.get_staff()
        fellows = people.get_fellows()
        walker = 0

        if self.occupant_type == 'STAFF':
            def staff_placement(self):
                for space in self.spaces_available:
                    for staff in staffs:
                        try:
                            Space.add_person(staff[walker])
                            walker+1
                        except:
                            continue
                        finally:
                            return "All staff have been allocated."
        elif self.occupant_type == 'FELLOW':
            def fellow_placement(self):
                for space in self.spaces_available:
                    for fellow in fellows:
                        try:
                            Space.add_person(fellow[walker])
                            walker+1
                        except:
                            continue
                        finally:
                            return "All fellows have been allocated."

        def __repr__(self):
            return "{}".format(self.name)


class LivingSpace(Space):
    def __init__(self, name, type, occupant_type):
        Space.__init__(self, name, type, occupant_type)
        self.limit = 4
        people = PeopleFile().read_file()
        males = people.get_male_residential_fellows()
        females = people.get_female_residential_fellows()
        walker = 0

        if LivingSpace.occupant_type == 'MALE':
            def male_placement(self):
                for space in self.spaces_available:
                    for male in males:
                        try:
                            Space.add_person(male[walker])
                            walker+1
                        except:
                            continue
                        finally:
                            return "All males have been allocated."
        elif LivingSpace.occupant_type == 'FEMALE':
            def female_placement(self):
                for space in self.spaces_available:
                    for female in females:
                        try:
                            Space.add_person(female[walker])
                            walker+1
                        except:
                            continue
                        finally:
                            return "All females have been allocated."

        def __repr__(self):
            return "{}".format(self.name)

sp = Space
print sp.list_spaces
print sp.list_people
