from amity import Office, Room, Amity


class StaffOffices:
    """Staff offices instantiation class"""
    def __init__(self):
        furnace = Office('furnace')
        gild = Office('Gild')
        hacksaw = Office('Hacksaw')
        self.spaces_available = [furnace, gild, hacksaw]

    def place_staff_in_offices(self):
        """method for placing staff"""
        return Amity.place_people_in_spaces(self.spaces_available, 'staff')

    def number_of_offices(self):
        return len(self.spaces_available)


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
        self.spaces_available = [cedar, carat, kiln, anvil, crucible, foundry, sledgehammer]

    def place_fellows_in_offices(self):
        """method for placing fellows in offices"""
        return Amity.place_people_in_spaces(self.spaces_available, 'fellows')

    def number_of_offices(self):
        return len(self.spaces_available)


class MaleRooms:
    def __init__(self):
        olive = Room('Olive')
        tongs = Room('Tongs')
        mahogany = Room('Mahogany')
        sapele = Room('Sapele')
        maple = Room('Maple')
        konoha = Room('Konoha')
        self.spaces_available = [olive, tongs, mahogany, sapele, maple, konoha]

    def place_male_fellows_in_rooms(self):
        return Amity.place_people_in_spaces(self.spaces_available, 'male_fellows')

    def number_of_rooms(self):
        return len(self.spaces_available)


class FemaleRooms:
    def __init__(self):
        iroko = Room('Iroko')
        obeche = Room('obeche')
        juniper = Room('Juniper')
        aishte = Room('Aishte')
        self.spaces_available = [iroko, obeche, juniper, aishte]

    def place_female_fellows_in_rooms(self):
        return Amity.place_people_in_spaces(self.spaces_available, 'female_fellows')

    def number_of_rooms(self):
        return len(self.spaces_available)
