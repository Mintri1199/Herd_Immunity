import unittest
from simulation import Simulation
from person import Person


class SimulationTest(unittest.TestCase):
    def setUp(self):
        self.new_sim = Simulation(10000, 0.25, "Ebola", 0.5, 0.25, 100)

    def test_create_population_method(self):
        infected_count = 0

        self.new_sim._create_population()
        assert len(self.new_sim.population) == 10000

        for person in self.new_sim.population:
            if person.infection is not None:
                infected_count += 1

        assert infected_count == 100

