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
        staffs = []
        for person in self:
            if isinstance(person, Staff):
                staffs.append(person)
        return [staff for staff in staffs]

    def get_fellows(self):
        fellows = []
        for person in self:
            if isinstance(person, Fellow):
                fellows.append(person)
        return [fellow for fellow in fellows]

    def get_male_residential_fellows(self):
        male_residential_fellows = []
        for person in self:
            if isinstance(person, Fellow) and person.gender == 'M' and person.need == 'Y':
                male_residential_fellows.append(person)
        return [male for male in male_residential_fellows]

    def get_female_residential_fellows(self):
        female_residential_fellows = []
        for person in self:
            if isinstance(person, Fellow) and person.gender == 'F' and person.need == 'Y':
                female_residential_fellows.append(person)
        return [female for female in female_residential_fellows]
