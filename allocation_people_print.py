from allocation_people_input_class import PeopleFile

people_collection = PeopleFile().read_file()
people_collection.return_staff()
print people_collection.get_fellows()
print people_collection.get_male_residential_fellows()
