from allocation_people_input_class import PeopleFile
from allocation_spaces import Office


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
        return Office.place_people_in_offices(self.offices_available, 'fellows')

    def number_of_offices(self):
        return len(self.offices_available)
