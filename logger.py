class Logger(object):

    def __init__(self, file_name):

        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        first_line = str(("{} {} {} {} {}\n".format(pop_size, vacc_percentage,
                                          virus_name, mortality_rate,
                                          basic_repro_num))).replace(" ", "    ")

        with open(self.file_name, "w") as file:
            file.write(first_line)

    def log_interaction(self, person1=object, person2=object, did_infect=bool, person2_vacc=bool, person2_sick=bool):
        with open(self.file_name, "a") as file:
            if did_infect:
                file.write("{} has infected {}\n".format(person1._id, person2._id))
            else:
                if person2_sick:
                    file.write("{} is already sick\n". format(person2._id))
                elif person2_vacc:
                    file.write("{} is vaccinated\n".format(person2._id))
                else:
                    file.write("{} fails to infect {}\n".format(person1._id, person2._id))

    def log_infection_survival(self, person, did_die_from_infection):
        pass

    def log_time_step(self, time_step_number):
        pass
