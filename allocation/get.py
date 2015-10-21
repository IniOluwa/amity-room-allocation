"""
All allocation results.
"""
from manager import Manager

manager = Manager()
manager.space_placing()
spaces = manager.list_spaces()


class Allocations(object):
    def get_allocated_fellows(self):
        """Return of spaces populated with fellows and staff"""
        print "All allocated fellows and staff are as follows"
        for index in range(len(spaces)-1):
            manager.allocation()
            if spaces[index].occupant_type == 'STAFF':
                print spaces[index], "- STAFF OFFICE"
                print spaces[index].list_people()
            elif spaces[index].occupant_type == 'FELLOW':
                print spaces[index], "- FELLOW OFFICE"
                print spaces[index].list_people()
            elif spaces[index].occupant_type == 'MALE':
                print spaces[index], "- MALE ROOM"
                print spaces[index].list_people()
            elif spaces[index].occupant_type == 'FEMALE':
                print spaces[index], "- FEMALE ROOM"
                print spaces[index].list_people()

    def get_unallocated_fellows(self):
        """Return unallocated fellows"""
        print "All unallocated fellows are as follows"
        manager.unallocated_fellows()

allocation = Allocations()
allocation.get_allocated_fellows()
allocation.get_unallocated_fellows()
