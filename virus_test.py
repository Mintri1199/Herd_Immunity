from virus import Virus
import unittest


class VirusTest(unittest.TestCase):

    def test_virus_instantiation(self):
        ebola = Virus("Ebola", 0.7, 0.25)
        assert ebola.name == "Ebola"
        assert  ebola.mort_rate == 0.7
        assert ebola.repro_rate == 0.25
