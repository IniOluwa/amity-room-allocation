from allocation_allocate_male_fellows_to_rooms import MaleRooms
from allocation_allocate_female_fellows_to_rooms import FemaleRooms
from allocation_allocate_staff import StaffOffices
from allocation_allocate_fellows import FellowsOffices


class Print:

    def allocate_staff_to_offices(self):
        staff = StaffOffices()
        for index in range(staff.number_of_offices()):
            print "STAFF OFFICE"
            print staff.place_staff_in_offices()[index]
            print staff.place_staff_in_offices()[index].list_persons()

    def allocate_fellows_to_offices(self):
        fellows = FellowsOffices()
        for index in range(fellows.number_of_offices()):
            print "FELLOWS OFFICE"
            print fellows.place_fellows_in_offices()[index]
            print fellows.place_fellows_in_offices()[index].list_persons()

    def allocate_male_fellows_to_rooms(self):
        males = MaleRooms()
        for index in range(males.number_of_rooms()):
            print "MALE ROOM"
            print males.place_male_fellows_in_rooms()[index]
            print males.place_male_fellows_in_rooms()[index].list_persons()

    def allocate_female_fellows_to_rooms(self):
        females = FemaleRooms()
        for index in range(females.number_of_rooms()):
            print "FEMALE ROOM"
            print females.place_female_fellows_in_rooms()[index]
            print females.place_female_fellows_in_rooms()[index].list_persons()

Print().allocate_staff_to_offices()