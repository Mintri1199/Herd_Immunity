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
            else:
                self.population.append(Person(self.next_person_id, False, None))
                self.next_person_id += 1

    # Flag for the run method
    def _simulation_should_continue(self):
        self.current_infected = 0  # Reset the variable
        death = 0

        for person in self.population:
            if person.is_alive is False:
                death += 1

        for person in self.population:  # Recount the infected population ignoring the dead ones
            if person.infection and person.is_alive:
                self.current_infected += 1

        self.total_infected = self.current_infected  # Set the total infected population

        if death == len(self.population):
            return False
        if self.total_infected == 0:
            return False
        else:
            return True

    def run(self):
        time_step_counter = 0
        should_continue = True
        self._create_population()

        while should_continue:
            # Initiate interaction with 100 people for each person
            self.time_step()

            # Check if anyone died after interacting with 100 people
            for person in self.population:
                person.did_survive_infection()
                self.logger.log_infection_survival(person, person.is_alive)

            should_continue = self._simulation_should_continue()
            self.logger.log_time_step(time_step_counter)
            time_step_counter += 1

        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
        number_of_interaction = 1
        for person in self.population:
            while number_of_interaction <= 100:
                rando = random.choice(self.population)
                # Prevent interaction with dead corpse and with it self
                while rando.is_alive is False or rando._id == person._id:
                    rando = random.choice(self.population)

                self.interaction(person, rando)
                number_of_interaction += 1
            number_of_interaction = 1

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


new_simulation = Simulation(500, 0.90, "Ebola", 0.70, 0.25, 100)
new_simulation.run()