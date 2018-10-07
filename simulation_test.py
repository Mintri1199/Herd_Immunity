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

    def test_should_continue_method(self):
        self.new_sim._create_population()
        assert self.new_sim._simulation_should_continue() is True

    def test_should_continue_method_deaths_case(self):
        self.new_sim._create_population()

        for person in self.new_sim.population:
            person.is_alive = False
        assert self.new_sim._simulation_should_continue() is False

    def test_should_continue_method_cure_case(self):
        self.new_sim._create_population()

        for person in self.new_sim.population:
            person.is_alive = True
            person.infection = None
            person.is_vaccinated = True
        assert self.new_sim._simulation_should_continue() is False

    def test_newly_infected_method_empty_list(self):
        self.new_sim._create_population()
        self.new_sim.newly_infected = [10000, 9999, 9998, 9997]
        self.new_sim._infect_newly_infected()
        assert len(self.new_sim.newly_infected) == 0

    def test_newly_infected_method(self):
        list = [10000, 9999, 9998, 9997]
        self.new_sim.newly_infected = list
        self.new_sim._infect_newly_infected()

        for id in list:
            for person in self.new_sim.population:
                if person._id == id:
                    assert person.infection is not None
