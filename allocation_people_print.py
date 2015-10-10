from allocation_allocate_male_fellows_to_rooms import MaleRooms
from allocation_allocate_female_fellows_to_rooms import FemaleRooms
from allocation_allocate_staff import StaffOffices
from allocation_allocate_fellows import FellowsOffices

females = FemaleRooms()
males = MaleRooms()
staff = StaffOffices()
fellows = FellowsOffices()


for index in range(fellows.number_of_offices()):
    print fellows.place_fellows_in_offices()[index]
    print fellows.place_fellows_in_offices()[index].list_persons()

for index in range(staff.number_of_offices()):
    print staff.place_staff_in_offices()[index]
    print staff.place_staff_in_offices()[index].list_persons()

for index in range(males.number_of_rooms()):
    print males.place_male_fellows_in_rooms()[index]
    print males.place_male_fellows_in_rooms()[index].list_persons()

for index in range(females.number_of_rooms()):
    print females.place_female_fellows_in_rooms()[index]
    print females.place_female_fellows_in_rooms()[index].list_persons()
