import random
from person import Person
# Указаны типы персонажей и их возможные параметры

type_person = {
    "warrior" : {                       # Тип - Воин
        "strength": 30,                 # Сила
        "agility": 10,                  # Ловкость
        "intellect": 5,                 # Интеллект
        "initiative": 0,                # Инициатива
        "health": 20,                   # Здоровье
        "energy": 5,                    # Энергия
        "persistence": 5,               # Стойкость
        "reaction": 3,                  # Реакция
        "consciousness": 0,             # Сознание
        "burden": 0,                    # Ноша
        "athletics": 0,                 # Навык - Атлетика
        "no_weapons": 25,               # Навык - Без оружия
        "endurance": 0,                 # Навык - Выносливость
        "throwing": 15,                 # Навык - Метание
        "heavy_weapon": 25,             # Навык - Тяжёлое оружие
        "cold_weapon": 25,              # Навык - Холодное оружие
        "gambl": 0,                     # Навык - Азартные игры
        "acrobatics": 5,                # Навык - Акробатика
        "theft": 0,                     # Навык - Воровство
        "light_weapon": 25,             # Навык - Лёгкое оружие
        "traps": 0,                     # Навык - Ловушки
        "observation": 0,               # Навык - Наблюдательность
        "hack": 0,                      # Навык - Взлом
        "hightech_weapons": 0,          # Навык - Высокотехнологичное оружие
        "engineering": 0,               # Навык - Инженерия
        "medicine": 0,                  # Навык - Медицина
        "negotiation": 5,               # Навык - Переговоры
        "trade": 0,                     # Навык - Торговля
    }
}

def create_person(type: str, level: int = 1):

    if type in type_person:
        person = Person(name="MyPers_1", level=level)

        parameter_priority = {k: v for k, v in sorted(type_person[type].items(),
                                                      key=lambda item: item[1],
                                                      reverse=True)}
        # Указано для теста проверки сортировки
        print(parameter_priority)

        max_random = 0
        for value in type_person[type].values():
            max_random += value

        while person.bounty > 0:

            chance = random.randrange(0, max_random, 1)

            current_chance = 0
            current_key = ""

            for key, value in type_person[type].items():
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