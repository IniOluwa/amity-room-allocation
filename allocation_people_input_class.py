from allocation_person_class import Staff, Fellow
from allocation_people_collection import PeopleCollection


class PeopleFile(object):
    """Class for getting and sorting people according to role"""

    def read_file(self):
        people = open('people.txt')
        people_collection = PeopleCollection()

        for line in iter(people):
            """breaking line into list"""
            line = line.split()
            """Assigning objects in list positions values to their respective values"""
            firstname = line[0]
            lastname = line[1]
            role = line[2]

            if role == 'STAFF':
                """Instantiation of a single staff"""
                staff = Staff(firstname, lastname, role)
                people_collection.append(staff)

            elif role == 'FELLOW':
                gender = line[3]
                need = line[4]
                """Instantiation of a single fellow"""
                fellow = Fellow(firstname, lastname, role, gender, need)
                people_collection.append(fellow)

        return people_collection
