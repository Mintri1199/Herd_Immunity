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
        self.vacc_percentage = vacc_percentage
        self.mortality_rate = mortality_rate
        self.population = []
        self.virus_name = virus_name
        self.current_death = 0
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus = Virus(virus_name, mortality_rate, basic_repro_num)
        self.basic_repro_num = basic_repro_num
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

            elif random.random() < self.vacc_percentage:
                self.population.append(Person(self.next_person_id, True, None))
                self.next_person_id += 1

            else:

                self.population.append(Person(self.next_person_id, False, None))
                self.next_person_id += 1


    # Flag for the run method
    def _simulation_should_continue(self):
        self.current_infected = 0  # Reset the variable
        self.current_death = 0
        for person in self.population:
            if person.is_alive is False:
                self.current_death += 1

        for person in self.population:  # Recount the infected population ignoring the dead ones
            if person.infection and person.is_alive:
                self.current_infected += 1

        self.total_death = self.current_death

        if self.current_death == len(self.population):
            return False
        if self.current_infected == 0:
            return False
        else:
            return True

    def run(self):
        time_step_counter = 0

        self._create_population()

        should_continue = self._simulation_should_continue()
        self.logger.write_metadata(self.population_size, self.vacc_percentage,
                                   self.virus_name, self.basic_repro_num, self.mortality_rate)
        while should_continue:
            self.total_infected = 0
            # Initiate interaction with 100 people for each person
            self.time_step()

            # Check if anyone died after interacting with 100 people
            for person in self.population:
                self.logger.log_infection_survival(person, person.did_survive_infection())

            self._infect_newly_infected()

            for person in self.population:
                if person.infection is not None:
                    self.total_infected += 1

            print(self.total_infected)

            should_continue = self._simulation_should_continue()

            self.logger.log_time_step(time_step_counter)
            time_step_counter += 1
        print("{} people died".format(self.total_death))
        print('The simulation has ended after {} turns.'.format(time_step_counter - 1))

    def time_step(self):
        number_of_interaction = 1
        for person in self.population:
            if person.is_alive is True:
                while number_of_interaction <= 100:
                    rando = random.choice(self.population)
                    # Prevent interaction with dead corpse and with it self
                    while rando.is_alive is False or rando._id == person._id:
                        rando = random.choice(self.population)

                    self.interaction(person, rando)
                    number_of_interaction += 1
                number_of_interaction = 1
            else:
                pass

    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated:
            self.logger.log_interaction(person, random_person, False, True, False)
        if random_person.infection is not None:
            self.logger.log_interaction(person, random_person, False, False, True)
        else:
            if random.random() < self.basic_repro_num:
                self.logger.log_interaction(person, random_person, True, False, False)
                self.newly_infected.append(random_person._id)
            else:
                self.logger.log_interaction(person, random_person, False, False, False)

    def _infect_newly_infected(self):
        for id in self.newly_infected:
            for person in self.population:
                if person._id == id:
                    person.infection = self.virus
        self.newly_infected = []


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