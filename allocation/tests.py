import unittest
from person import Person, Staff, Fellow
from inputting import PeopleFile
from collection import PeopleCollection
from amity import Office, Room
from allocation import StaffOffices, FellowsOffices, MaleRooms, FemaleRooms

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


class TestFellowsAllocation(unittest.TestCase):
    """Unittest for fellows allocation"""
    def setUp(self):
        self.fellows_offices = FellowsOffices()
        self.office_number = self.fellows_offices.number_of_offices()

    def test_for_fellows_offices(self):
        self.assertEqual(self.office_number, 7)


class TestStaffAllocation(unittest.TestCase):
    """unittest for staff allocation"""
    def setUp(self):
        self.staff_offices = StaffOffices()
        self.office_number = self.staff_offices.number_of_offices()

    def test_for_staff_offices(self):
        self.assertEqual(self.office_number, 3)


class TestMaleRoomAllocation(unittest.TestCase):
    """Unittest for male rooms allocation"""
    def setUp(self):
        self.male_rooms = MaleRooms()
        self.male_rooms_number = self.male_rooms.number_of_rooms()

    def test_for_number_of_male_rooms(self):
        self.assertEqual(self.male_rooms_number, 6)


class TestFemaleRoomAllocation(unittest.TestCase):
    """Unittest for male rooms allocation"""
    def setUp(self):
        self.female_rooms = FemaleRooms()
        self.female_rooms_number = self.female_rooms.number_of_rooms()

    def test_for_number_of_female_rooms(self):
        self.assertEqual(self.female_rooms_number, 4)


class TestOffices(unittest.TestCase):
    """Unitest for offices"""

    def setUp(self):
        self.office = Office
        self.cedar = Office('Cedar')
        self.person = Person('susan', 'adelokiki')

    def test_that_offices_can_be_created(self):
        self.assertIsInstance(self.cedar, self.office)
        self.assertEqual(self.cedar.name, 'Cedar')
        self.assertEqual(self.cedar.limit, 6)

    def test_that_a_person_can_be_added_to_office(self):
        self.assertEqual(len(self.cedar.people), 0)
        self.cedar.add_person(self.person)
        self.assertIn(self.person, self.cedar.people)
        self.assertEqual(len(self.cedar.people), 1)


class TestRooms(unittest.TestCase):
    """Unitest for offices"""

    def setUp(self):
        self.room = Room
        self.crucible = Room('Crucible')
        self.person = Person('stephen', 'sunday')

    def test_that_offices_can_be_created(self):
        self.assertIsInstance(self.crucible, self.room)
        self.assertEqual(self.crucible.name, 'Crucible')
        self.assertEqual(self.crucible.limit, 4)

    def test_that_a_person_can_be_added_to_office(self):
        self.assertEqual(len(self.crucible.people), 0)
        self.crucible.add_person(self.person)
        self.assertIn(self.person, self.crucible.people)
        self.assertEqual(len(self.crucible.people), 1)


if __name__ == '__main__':

    unittest.main()
