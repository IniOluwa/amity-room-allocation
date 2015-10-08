from allocation_people_input_class import PeopleFile

people_collection = PeopleFile().read_file()
people_collection.return_staff()
people_collection.return_fellows()
