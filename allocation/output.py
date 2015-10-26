"""
All allocation results.
"""
from models.manager import Manager

manager = Manager()
manager.space_placing()
spaces = manager.list_spaces()
manager.allocation()


class Allocations(object):
    def get_allocated_fellows(self):
        """Return of spaces populated with fellows and staff"""
        print "All allocated fellows and staff are as follows"
        for index in range(len(spaces)-1):
            if spaces[index].space_type == 'OFFICE':
                print spaces[index], "- OFFICE"
                print spaces[index].list_people()

            elif spaces[index].occupant_type == 'MALE':
                print spaces[index], "- MALE ROOM"
                print spaces[index].list_people()

            elif spaces[index].occupant_type == 'FEMALE':
                print spaces[index], "- FEMALE ROOM"
                print spaces[index].list_people()

    def get_unallocated_fellows(self):
        """Return unallocated fellows"""
        print "All unallocated staff are as follows:"
        print manager.unallocated_staff
        print "All fellows lacking office spaces are as follows:"
        print manager.unallocated_fellows_to_officespaces
        print "All fellows lacking living spaces are as follows:"
        print manager.unallocated_fellows_to_livingspaces


"""Call allocation methods"""
allocation = Allocations()
allocation.get_allocated_fellows()
allocation.get_unallocated_fellows()
