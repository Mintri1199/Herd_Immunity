from person import Person
from logger import Logger
from virus import Virus
import random, sys
random.seed(42)


class Simulation(object):

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):

        self.initial_infected = initial_infected
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus = Virus(virus_name, mortality_rate, basic_repro_num)

        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)

        self.logger = Logger(self.file_name)
        self.newly_infected = []

    # Creating person objects to match the population size
    def _create_population(self):
        infected_count = 0
        while len(self.population) != self.population_size:
            if infected_count != self.initial_infected:
                self.population.append(Person(self.next_person_id, False, self.virus))
                infected_count += 1
                self.next_person_id += 1
            else:
                self.population.append(Person(self.next_person_id, False, None))
                self.next_person_id += 1

        self.current_infected = infected_count

    def _simulation_should_continue(self):

        pass

    def run(self):
        time_step_counter = 0
        should_continue = None
        while should_continue:
            pass
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
            pass

    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True
        pass

    def _infect_newly_infected(self):
        pass


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()