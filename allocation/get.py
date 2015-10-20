from manager import Manager

manager = Manager()
manager.space_placing()
spaces = manager.list_spaces()


for index in range(len(spaces)-1):
    if spaces[index].occupant_type == 'STAFF':
        manager.allocate()
        print spaces[index], "- STAFF OFFICE"
        print spaces[index].list_people()
    elif spaces[index].occupant_type == 'FELLOW':
        manager.allocate()
        print spaces[index], "- FELLOW OFFICE"
        print spaces[index].list_people()
    elif spaces[index].occupant_type == 'MALE':
        manager.allocate()
        print spaces[index], "- MALE ROOM"
        print spaces[index].list_people()
    elif spaces[index].occupant_type == 'FEMALE':
        manager.allocate()
        print spaces[index], "- FEMALE ROOM"
        print spaces[index].list_people()
