from person import Person
from virus import Virus
import unittest


class PersonTest(unittest.TestCase):
    # Set up the virus objects for tests
    def setUp(self):
        self.weak_virus = Virus("Weak", 0, 0)
        self.deadly_virus = Virus("Deadly", 0.99, 0.99)


    # Checking the instantiation of person object with virus
    def test_person_instantiation(self):
        new_person = Person(1, False, self.weak_virus)
        assert new_person.infection is self.weak_virus
        assert new_person.is_alive is True
        assert new_person._id is 1
        assert new_person.is_vaccinated is False

    # Check two cases of person objects
    def test_did_survive_method(self):
        dying_person = Person(1, False, self.deadly_virus)
        healthy_person = Person(2, False, self.weak_virus)

        assert dying_person.did_survive_infection() is False
        assert dying_person.is_alive is False
        assert dying_person.infection is not None

        assert healthy_person.did_survive_infection() is True
        assert healthy_person.is_alive is True
        assert healthy_person.infection is None
