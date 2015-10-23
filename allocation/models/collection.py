"""
A PeopleCollection class that has the attributes of a list,
this class sorts all the instances that has been created in PeopleFIle,
and separates staff from fellows.
"""
from person import Staff, Fellow


class PeopleCollection(list):
    """People collection class for collecting instantiated people
    and sorting them into fellows and staff according to instantiation"""
    def get_staff(self):
        for person in self:
            if isinstance(person, Staff):
                yield person

    def get_fellows(self):
        for person in self:
            if isinstance(person, Fellow):
                yield person

    def get_male_residential_fellows(self):
        for person in self:
            if isinstance(person, Fellow) and person.gender == 'M' and person.need == 'Y':
                yield person

    def get_female_residential_fellows(self):
        for person in self:
            if isinstance(person, Fellow) and person.gender == 'F' and person.need == 'Y':
                yield person
