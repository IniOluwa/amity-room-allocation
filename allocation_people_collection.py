from allocation_person_class import Staff, Fellow


class PeopleCollection(list):
    """People collection class for collecting instantiated people and sorting them into fellows and staff according to instantiation"""
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

    def return_fellows(self):
        for i in self.get_fellows():
            print (i.firstname + ' ' + i.lastname)

    def return_staff(self):
        for i in self.get_staff():
            print (i.firstname + ' ' + i.lastname)

    def return_male_residential_fellows(self):
        for i in self.get_male_residential_fellows():
            print (i.firstname + ' ' + i.lastname)
