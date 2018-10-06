class Logger(object):

    def __init__(self, file_name):

        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        first_line = str(("{} {} {} {} {}".format(pop_size, vacc_percentage,
                                          virus_name, mortality_rate,
                                          basic_repro_num))).replace(" ", "    ")

        with open(self.file_name, "w") as file:
            file.write(first_line)

    def log_interaction(self, person1, person2, did_infect=None,
                        person2_vacc=None, person2_sick=None):
        pass

    def log_infection_survival(self, person, did_die_from_infection):
        pass

    def log_time_step(self, time_step_number):
        pass
