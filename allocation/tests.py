"""
Unittests for Amity allocation
"""
import unittest
from person import Person, Staff, Fellow
from inputting import PeopleFile
from collection import PeopleCollection
from manager import Manager
from spaces import OfficeSpace, LivingSpace


class TestPersonInstantiation(unittest.TestCase):
    """Unittest for person, staff and fellow instantiation"""
    def setUp(self):
        self.person = Person
        self.staff = Staff
        self.fellow = Fellow
        self.ini = Person('IniOluwa', 'Fageyinbo')
        self.chidi = Staff('Chidiebere', 'Nnadi', 'STAFF')
        self.uzochikwa = Fellow('Uzochikwa', 'Awili', 'FELLOW', 'M', 'Y')

    def test_person_instantiation(self):
        self.assertIsInstance(self.ini, self.person)
        self.assertEqual(self.ini.firstname, 'IniOluwa')
        self.assertEqual(self.ini.lastname, 'Fageyinbo')

    def test_staff_instantiation(self):
        self.assertIsInstance(self.chidi, self.staff)
        self.assertEqual(self.chidi.firstname, 'Chidiebere')
        self.assertEqual(self.chidi.lastname, 'Nnadi')
        self.assertEqual(self.chidi.role, 'STAFF')

    def test_fellow_instantiation(self):
        self.assertIsInstance(self.uzochikwa, self.fellow)
        self.assertEqual(self.uzochikwa.firstname, 'Uzochikwa')
        self.assertEqual(self.uzochikwa.lastname, 'Awili')
        self.assertEqual(self.uzochikwa.role, 'FELLOW')
        self.assertEqual(self.uzochikwa.gender, 'M')
        self.assertEqual(self.uzochikwa.need, 'Y')


class TestForPeopleInputAndUse(unittest.TestCase):
    """Unittest for people collection"""
    def setUp(self):
        self.people = PeopleFile()
        self.people_file = self.people.read_file()
        self.people_collect = PeopleCollection

    def test_for_people_collection_in_read_file(self):
        self.assertIsInstance(self.people_file, self.people_collect)


class TestOffices(unittest.TestCase):
    """Unitest for offices"""

    def setUp(self):
        self.office = OfficeSpace
        self.cedar = OfficeSpace('Cedar', 'OFFICE', 'FELLOW')
        self.person = Person('susan', 'adelokiki')

    def test_that_a_person_can_be_added_to_office(self):
        self.assertEqual(len(self.cedar.people), 0)
        self.cedar.add_person(self.person)
        self.assertIn(self.person, self.cedar.people)
        self.assertEqual(len(self.cedar.people), 1)


class TestRooms(unittest.TestCase):
    """Unitest for offices"""

    def setUp(self):
        self.room = LivingSpace
        self.crucible = LivingSpace('Crucible', 'ROOM', 'MALE')
        self.person = Person('stephen', 'sunday')

    def test_that_a_person_can_be_added_to_office(self):
        self.assertEqual(len(self.crucible.people), 0)
        self.crucible.add_person(self.person)
        self.assertIn(self.person, self.crucible.people)
        self.assertEqual(len(self.crucible.people), 1)


if __name__ == '__main__':

    unittest.main()
