import random


class Person(object):
    # Necessary Attributes
    def __init__(self, _id, is_vaccinated=bool, infection=object):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection

    # Checking if the person survive the infection
    def did_survive_infection(self):
        if self.infection is not None:
            check_num = random.random()
            if check_num > self.infection.mort_rate:
                self.is_vaccinated = True
                self.infection = None
                return True

            else:
                self.is_alive = False
                return False
        else:
            return True
