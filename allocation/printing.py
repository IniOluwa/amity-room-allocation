from allocation import StaffOffices, FellowsOffices, MaleRooms, FemaleRooms

class Print:

    def allocate(self):
        digit = int(raw_input('Pick an option: '))
        staff = StaffOffices()
        staff_offices = staff.number_of_offices()
        fellows = FellowsOffices()
        fellows_offices = fellows.number_of_offices()
        male = MaleRooms()
        male_rooms = male.number_of_rooms()
        female = FemaleRooms()
        female_rooms = female.number_of_rooms()
        number = [staff_offices, fellows_offices, male_rooms, female_rooms]
        for num in number:
            if num == staff_offices:
                if digit == 1:
                    for index in range(staff_offices):
                        print staff.place_staff_in_offices()[index], "STAFF OFFICE"
                        print staff.place_staff_in_offices()[index].list_persons()
            elif num == fellows_offices:
                if digit == 2:
                    for index in range(fellows_offices):
                        print fellows.place_fellows_in_offices()[index], "FELLOWS OFFICE"
                        print fellows.place_fellows_in_offices()[index].list_persons()
            elif num == male_rooms:
                if digit == 3:
                    for index in range(male_rooms):
                        print male.place_male_fellows_in_rooms()[index], "MALE ROOM"
                        print male.place_male_fellows_in_rooms()[index].list_persons()
            elif num == female_rooms:
                if digit == 4:
                    for index in range(female_rooms):
                        print female.place_female_fellows_in_rooms()[index], "FEMALE ROOM"
                        print female.place_female_fellows_in_rooms()[index].list_persons()
