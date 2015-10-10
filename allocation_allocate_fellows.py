from allocation_people_input_class import PeopleFile


class Office:
    """Single office creation class"""
    def __init__(self, name):
        self.name = name
        self.limit = 6
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


class FellowsOffices:
    """Fellows offices instantiation class"""
    def __init__(self):
        cedar = Office('Cedar')
        carat = Office('Carat')
        kiln = Office('Kiln')
        anvil = Office('Anvil')
        crucible = Office('Crucible')
        foundry = Office('Foundry')
        sledgehammer = Office('sledgehammer')
        self.offices_available = [cedar, carat, kiln, anvil, crucible, foundry, sledgehammer]

    def place_fellows_in_offices(self):
        """method for placing fellows in offices"""
        fellows_list = PeopleFile().read_file().get_fellows()
        office_walker = 0
        for office in self.offices_available:
            for num in range(len(fellows_list)):
                try:
                    office.add_person(fellows_list[office_walker])
                except:
                    continue
                office_walker += 1
        return self.offices_available

    def number_of_offices(self):
        return len(self.offices_available)
