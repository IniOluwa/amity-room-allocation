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
        print "All unallocated fellows are as follows"
        manager.unallocated_fellows()

allocation = Allocations()
allocation.get_allocated_fellows()
allocation.get_unallocated_fellows()
