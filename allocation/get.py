from manager import Manager

manager = Manager()
manager.space_placing()
# print manager.list_spaces()

manager.staff_allocation()
print manager.get_staff_placement()[0], "- STAFF OFFICE"
print manager.get_staff_placement()[0].list_people()

manager.fellow_allocation()
print manager.get_fellow_placement()[0], "- FELLOW OFFICE"
print manager.get_fellow_placement()[0].list_people()

manager.male_allocation()
print manager.get_male_placement()[0], "- MALE ROOM"
print manager.get_male_placement()[0].list_people()

manager.female_allocation()
print manager.get_female_placement()[0], "- FEMALE ROOM"
print manager.get_female_placement()[0].list_people()
