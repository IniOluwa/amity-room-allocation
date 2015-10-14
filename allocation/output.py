from printing import Print

call = Print()
while True:
    print "Pick 1 to see staff allocation"
    print "Pick 2 to see fellows office allocation"
    print "Pick 3 to see male fellows room allocation"
    print "Pick 4 to see female fellows room allocation"
    print "Pick 5 to see all allocations"
    print "Pick 6 to close program"

    num = raw_input('what is your pick?:')
    if len(str(num)) < 1:
        print "Please pick a valid number"
    elif num.isalpha():
        print "Please pick a valid number"
    elif int(num) == 1:
        print call.allocate_staff_to_offices()
    elif int(num) == 2:
        print call.allocate_fellows_to_offices()
    elif int(num) == 3:
        print call.allocate_male_fellows_to_rooms()
    elif int(num) == 4:
        print call.allocate_female_fellows_to_rooms()
    elif int(num) == 5:
        print call.allocate_staff_to_offices()
        print call.allocate_fellows_to_offices()
        print call.allocate_male_fellows_to_rooms()
        print call.allocate_female_fellows_to_rooms()
    elif int(num) == 6:
        break
    else:
        print "Please pick a valid number"
