from allocation_people_input_class import PeopleFile


class Office:
    """Single office instantiation class"""
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


class StaffOffices:
    """Staff offices instantiation class"""
    def __init__(self):
        furnace = Office('furnace')
        gild = Office('Gild')
        hacksaw = Office('Hacksaw')
        self.offices_available = [furnace, gild, hacksaw]

    def place_staff_in_offices(self):
        """method for placing staff"""
        staff_list = PeopleFile().read_file().get_staff()
        office_walker = 0
        for office in self.offices_available:
            for num in range(len(staff_list)):
                try:
                    office.add_person(staff_list[office_walker])
                except:
                    continue
                office_walker += 1
        return self.offices_available

    def number_of_offices(self):
        return len(self.offices_available)
