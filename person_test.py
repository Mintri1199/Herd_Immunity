from person import Person
from virus import Virus
import unittest


class PersonTest(unittest.TestCase):

    def setUp(self):
        pass

    # Checking the instantiation of person object
    def test_person_instantiation(self):
        new_person = Person(1, False, None)
        assert new_person.infection is None
        assert new_person.is_alive is True
        assert new_person._id is 1
        assert new_person.is_vaccinated is False
