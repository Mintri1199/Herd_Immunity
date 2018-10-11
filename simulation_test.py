import unittest
import random
from simulation import Simulation


class SimulationTest(unittest.TestCase):
    def setUp(self):
        self.new_sim = Simulation(10000, 0.5, "Ebola", 0.5, 0.25, 100)
        self.smaller_sim = Simulation(10, 0.25, "Ebola", 0.5, 0.25, 5)

    def test_create_population_method(self):
        infected_count = 0
        vaccinated = 0
        self.new_sim._create_population()
        assert len(self.new_sim.population) == 10000

        for person in self.new_sim.population:
            if person.infection is not None:
                infected_count += 1

        assert infected_count == 100

        for person in self.new_sim.population:
            if person.is_vaccinated and person.infection is None:
                vaccinated += 1

        assert vaccinated == 4950

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

    def test_unique_interaction(self):
        self.smaller_sim._create_population()
        number_of_interaction = 1
        for person in self.smaller_sim.population:
            while number_of_interaction <= 100:
                rando = random.choice(self.smaller_sim.population)
                # Prevent interaction with dead corpse and with it self
                while rando.is_alive is False or rando._id == person._id:
                    rando = random.choice(self.smaller_sim.population)
                assert person._id is not rando._id
                assert rando.is_alive is True
                self.smaller_sim.interaction(person, rando)
                number_of_interaction += 1
            number_of_interaction = 1
