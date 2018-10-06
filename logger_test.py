from logger import Logger
from person import Person
from virus import Virus


deadly_virus = Virus("Deadly", 1, 1)
weak_virus  = Virus("Weak", 0, 0)

dummy  = Person(1, False, False)
dummy2 = Person(2, False, False)

dying_person = Person(3, False, deadly_virus)
healthy_person = Person(4, False, weak_virus)

new_log = Logger("logger_test.txt")
new_log.write_metadata(10000, 0.7, "Ebola", 0.5, 0.25)
# Record did infect = True
new_log.log_interaction(dummy, dummy2, True, False, False)

# Record did infect = False but vacc = True
new_log.log_interaction(dummy, dummy2, False, True, False)

# Record did infect = False but sick = True
new_log.log_interaction(dummy, dummy2, False, False, True)

# Record failure of infection
new_log.log_interaction(dummy, dummy2, False, False, False)

# Record the death of a person
new_log.log_infection_survival(dying_person, dying_person.did_survive_infection())

# Record the survival of a person
new_log.log_infection_survival(healthy_person, healthy_person.did_survive_infection())

# Record the time step
new_log.log_time_step(1)