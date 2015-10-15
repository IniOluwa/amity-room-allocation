"""
A class and method that prints out
people in rooms and offices in the right format.
"""
from allocation import StaffOffices, FellowsOffices, MaleRooms, FemaleRooms


class PrintPeople:

    def allocate_staff_to_offices(self):
        staff = StaffOffices()
        for index in range(staff.number_of_offices()):
            print staff.place_staff_in_offices()[index], "STAFF OFFICE"
            print staff.place_staff_in_offices()[index].list_persons()

    def allocate_fellows_to_offices(self):
        fellows = FellowsOffices()
        for index in range(fellows.number_of_offices()):
            print fellows.place_fellows_in_offices()[index], "FELLOWS OFFICE"
            print fellows.place_fellows_in_offices()[index].list_persons()

    def allocate_male_fellows_to_rooms(self):
        males = MaleRooms()
        for index in range(males.number_of_rooms()):
            print males.place_male_fellows_in_rooms()[index], "MALE ROOM"
            print males.place_male_fellows_in_rooms()[index].list_persons()

    def allocate_female_fellows_to_rooms(self):
        females = FemaleRooms()
        for index in range(females.number_of_rooms()):
            print females.place_female_fellows_in_rooms()[index], "FEMALE ROOM"
            print females.place_female_fellows_in_rooms()[index].list_persons()
