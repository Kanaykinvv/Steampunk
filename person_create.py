from person_type import types
from person import Person
import random


def create_person(type: str, level: int = 1):

    if type in types:
        person = Person(name="MyPers_1", level=level)

        parameter_priority = {k: v for k, v in sorted(types[type].items(),
                                                      key=lambda item: item[1],
                                                      reverse=True)}
        # Указано для теста проверки сортировки
        print(parameter_priority)

        max_random = 0
        for value in types[type].values():
            max_random += value

        while person.bounty > 0:

            chance = random.randrange(0, max_random, 1)

            current_chance = 0
            current_key = ""

            for key, value in types[type].items():
                current_chance += value
                if chance <= current_chance:
                    current_key = key
                    break

            person.parameter_up(name=current_key)

        return person
    else:
        return None


my_test_person = create_person(type="warrior", level=5)
print(my_test_person)
my_test_person.update_log_print()