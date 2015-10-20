from manager import Manager

manager = Manager()
manager.space_placing()
spaces = manager.list_spaces()
manager.staff_allocation()
manager.fellow_allocation()
manager.male_allocation()

for index in range(len(spaces)-1):
    if spaces[index].occupant_type == 'STAFF':
        print spaces[index], "- STAFF OFFICE"
        print spaces[index].list_people()


for index in range(len(spaces)-1):
    if spaces[index].occupant_type == 'FELLOW':
        print spaces[index], "- FELLOW OFFICE"
        print spaces[index].list_people()

for index in range(len(spaces)-1):
    if spaces[index].occupant_type == 'MALE':
        print spaces[index]
        print spaces[index].list_people


for index in range(len(spaces)-1):
    if spaces[index].occupant_type == 'FEMALE':
        print spaces[index]
        print spaces[index].list_people()
