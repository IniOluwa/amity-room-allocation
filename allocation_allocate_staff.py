from allocation_people_input_class import PeopleFile
from allocation_spaces import Office


class StaffOffices:
    """Staff offices instantiation class"""
    def __init__(self):
        furnace = Office('furnace')
        gild = Office('Gild')
        hacksaw = Office('Hacksaw')
        self.offices_available = [furnace, gild, hacksaw]

    def place_staff_in_offices(self):
        """method for placing staff"""
        return Office.place_fellows_in_offices(self.offices_available, 'staff')

    def number_of_offices(self):
        return len(self.offices_available)
