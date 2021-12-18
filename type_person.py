import random
from Person import Person
# Указаны типы персонажей и их возможные параметры

type_person = {
    "warrior" : {                       # Тип - Воин
        "strength": 30,                 # Сила
        "agility": 30,                  # Ловкость
        "intellect": 0,                 # Интеллект
        "initiative": 0,                # Инициатива
        "health": 0,                    # Здоровье
        "energy": 0,                    # Энергия
        "persistence": 0,               # Стойкость
        "reaction": 0,                  # Реакция
        "consciousness": 0,             # Сознание
        "burden": 0,                    # Ноша
        "athletics": 0,                 # Навык - Атлетика
        "no_weapons": 0,                # Навык - Без оружия
        "endurance": 0,                 # Навык - Выносливость
        "throwing": 0,                  # Навык - Метание
        "heavy_weapon": 0,              # Навык - Тяжёлое оружие
        "cold_weapon": 0,               # Навык - Холодное оружие
        "gambl": 0,                     # Навык - Азартные игры
        "acrobatics": 0,                # Навык - Акробатика
        "theft": 0,                     # Навык - Воровство
        "light_weapon": 0,              # Навык - Лёгкое оружие
        "traps": 0,                     # Навык - Ловушки
        "observation": 0,               # Навык - Наблюдательность
        "hack": 0,                      # Навык - Взлом
        "hightech_weapons": 0,          # Навык - Высокотехнологичное оружие
        "engineering": 0,               # Навык - Инженерия
        "medicine": 0,                  # Навык - Медицина
        "negotiation": 0,               # Навык - Переговоры
        "trade": 0,                     # Навык - Торговля
    }
}




def create_person(type: str, level: int = 1):

    if type in type_person:
        person = Person(name="MyPers_1", level=level)

        parameter_priority = {k: v for k, v in sorted(type_person[type].items(),
                                                      key=lambda item: item[1],
                                                      reverse=True)}
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

            if current_key == "strength":
                person.strength_up()
            elif current_key == "agility":
                person.agility_up()
            elif current_key == "intellect":
                person.intellect_up()
            elif current_key == "initiative":
                person.initiative_up()
            elif current_key == "health":
                person.health_up()
            elif current_key == "energy":
                person.energy_up()
            elif current_key == "persistence":
                person.persistence_up()
            elif current_key == "reaction":
                person.reaction_up()
            elif current_key == "consciousness":
                person.consciousness_up()

            elif current_key == "strength":
                person.strength_up()
            elif current_key == "strength":
                person.strength_up()
            elif current_key == "strength":
                person.strength_up()
            elif current_key == "strength":
                person.strength_up()