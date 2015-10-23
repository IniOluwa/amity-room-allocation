"""
The Person class, and the Staff and Fellow classes
which are both inheriting from the Person class.
"""


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
        self.has_officespace = False

    def __repr__(self):
        return "{0} {1}".format(self.firstname, self.lastname)


class Fellow(Person):
    """Class for a fellow(Inherting from the person class)"""
    def __init__(self, firstname, lastname, role, gender, need):
        Person.__init__(self, firstname, lastname)
        self.role = role
        self.gender = gender
        self.need = need
        self.has_officespace = False
        self.has_livingspace = False

    def __repr__(self):
        return "{0} {1}".format(self.firstname, self.lastname)
