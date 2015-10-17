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
        staff = []
        for i in self:
            if isinstance(i, Staff):
                staff.append(i)
        return staff

    def get_fellows(self):
        fellows = []
        for i in self:
            if isinstance(i, Fellow):
                fellows.append(i)
        return fellows

    def get_male_residential_fellows(self):
        male_residential_fellows = []
        for i in self:
            if isinstance(i, Fellow):
                if i.gender == 'M':
                    if i.need == 'Y':
                        male_residential_fellows.append(i)
        return male_residential_fellows

    def get_female_residential_fellows(self):
        female_residential_fellows = []
        for i in self:
            if isinstance(i, Fellow):
                if i.gender == 'F':
                    if i.need == 'Y':
                        female_residential_fellows.append(i)
        return female_residential_fellows

    def get_unallocated_fellows(self):
        unallocated_fellows = []
        for i in self:
            if isinstance(i, Fellow):
                if i.need == 'N':
                    unallocated_fellows.append(i)
        return unallocated_fellows
