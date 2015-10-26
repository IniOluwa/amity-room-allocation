"""
A PeopleFile class that gets the people,
creates instances of staff and fellows,
then appends them to a list.
"""
from person import Staff, Fellow
from collection import PeopleCollection
import os


class FileParser(object):
    """Class for getting and sorting people according to role"""

    @staticmethod
    def read_file(filename=os.path.join('data','people.txt')):
        people_collection = PeopleCollection()
        with open(filename) as people:
            for line in iter(people):
                """breaking line into list"""
                line = line.split()
                """Assigning objects in list positions
                values to their respective values"""
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
