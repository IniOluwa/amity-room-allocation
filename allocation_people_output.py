from allocation_people_print import Print

call = Print()
while True:
    print "Pick 1 to see staff allocation"
    print "Pick 2 to see fellows office allocation"
    print "Pick 3 to see male fellows room allocation"
    print "Pick 4 to see female fellows room allocation"
    print "Pick 5 to see all allocations"
    print "Pick 6 to close program"

    num = input('what is your pick?:')
    if num == 1:
        print call.allocate_staff_to_offices()
    elif num == 2:
        print call.allocate_fellows_to_offices()
    elif num == 3:
        print call.allocate_male_fellows_to_rooms()
    elif num == 4:
        print call.allocate_female_fellows_to_rooms()
    elif num == 5:
        print call.allocate_staff_to_offices()
        print call.allocate_fellows_to_offices()
        print call.allocate_male_fellows_to_rooms()
        print call.allocate_female_fellows_to_rooms()
    elif num == 6:
        break
