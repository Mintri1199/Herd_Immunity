import random
# TODO: Import the virus class


class Person(object):

    def __init__(self, _id, is_vaccinated=bool, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection

    # Checking if the person survive the infection
    def did_survive_infection(self):
        if self.infection is not None:
            check_num = random.uniform(0, 1)
            if check_num < self.infection.mort_rate:
                self.is_alive = False
                return False

            else:
                self.is_vaccinated = True
                self.infection = None
                return True
