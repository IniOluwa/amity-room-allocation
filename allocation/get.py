from manager import Manager

manager = Manager()
manager.space_placing()
print manager.list_spaces()

print manager.staff_allocation()
print manager.get_staff_placement()[0].list_people()

print manager.fellow_allocation()
print manager.get_fellow_placement()[0].list_people()

print manager.male_allocation()
print manager.get_male_placement()[0].list_people()

print manager.female_allocation()
print manager.get_female_placement()[0].list_people()
