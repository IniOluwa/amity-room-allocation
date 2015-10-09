class Person(object):
    """Class for a single person"""
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Staff(Person):
    """Class for a staff(Inherting from the person class)"""
    def __init__(self, firstname, lastname, role):
        Person.__init__(self, firstname, lastname)
        self.role = role

    def __repr__(self):
        return "{0} {1}".format(self.firstname, self.lastname)


class Fellow(Person):
    """Class for a fellow(Inherting from the person class)"""
    def __init__(self, firstname, lastname, role, gender, need):
        Person.__init__(self, firstname, lastname)
        self.role = role
        self.gender = gender
        self.need = need

    def __repr__(self):
        return "{0} {1}".format(self.firstname, self.lastname)


class MaleFellow(Person):
    """Class for a male fellow(Inherting from the person class)"""
    def __init__(self, role, gender, need):
        Person.__init__(self, self.firstname, self.lastname)
        self.role = role
        self.gender = gender
        self.need = need

    def __repr__(self):
        return "{0} {1}".format(self.firstname, self.lastname)


class FemaleFellow(Person):
    """Class for a female fellow(Inherting from the person class)"""
    def __init__(self, role, gender, need):
        Person.__init__(self, self.firstname, self.lastname)
        self.role = role
        self.gender = gender
        self.need = need

    def __repr__(self):
        return "{0} {1}".format(self.firstname, self.lastname)
