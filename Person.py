from game_config import *

class Person:

    name = ""                           # Имя персонажа
    cash = 0.0                          # Количество денежных средств
    experience = 0                      # Количество текущего опыта
    level = 1                           # Текущий уровень
    dice = "1D4"                        # Текущий кубик
    bounty = 0                          # Текущие очки развития

    strength_bonus = 0                  # Сила (бонус)
    strength_add = 0                    # Сила (улучшение)

    agility_bonus = 0                   # Ловкость (бонус)
    agility_add = 0                     # Ловкость (улучшение)

    intellect_bonus = 0                 # Интеллект (бонус)
    intellect_add = 0                   # Интеллект (улучшение)

    initiative_bonus = 0                # Инициатива (бонус)
    initiative_add = 0                  # Инициатива (улучшение)
    initiative_effect = 0               # Инициатива (эффект)

    health_current = 0                  # Здоровье (текущее)
    health_bonus = 0                    # Здоровье (бонус)
    health_add = 0                      # Здоровье (улучшение)
    health_effect = 0                   # Здоровье (эффект)

    energy_current = 0                  # Энергия (текущая)
    energy_bonus = 0                    # Энергия (бонус)
    energy_add = 0                      # Энергия (улучшение)
    energy_effect = 0                   # Энергия (эффект)

    persistence_bonus = 0               # Стойкость (бонус)
    persistence_add = 0                 # Стойкость (улучшение)
    persistence_effect = 0              # Стойкость (эффект)

    reaction_bonus = 0                  # Реакция (бонус)
    reaction_add = 0                    # Реакция (улучшение)
    reaction_effect = 0                 # Реакция (эффект)

    consciousness_bonus = 0             # Сознание (бонус)
    consciousness_add = 0               # Сознание (улучшение)
    consciousness_effect = 0            # Сознание (эффект)

    burden_current = 0                  # Ноша (текущая)
    burden_bonus = 0                    # Ноша (бонус)
    burden_add = 0                      # Ноша (улучшение)
    burden_effect = 0                   # Ноша (эффект)

    equipment = {}                      # Экипировка

    skills = {
        # Навык - Атлетика
        "Athletics":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Без оружия
        "NoWeapons":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Выносливость
        "Endurance":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Метание
        "Throwing":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Тяжёлое оружие
        "HeavyWeapon":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Холодное оружие
        "ColdWeapon":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Азартные игры
        "Gambl":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Акробатика
        "Acrobatics":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Воровство
        "Theft":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Лёгкое оружие
        "LightWeapon":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Ловушки
        "Traps":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Наблюдательность
        "Observation":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Взлом
        "Hack":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Высокотехнологичное оружие
        "HightechWeapons":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Инженерия
        "Engineering":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Медицина
        "Medicine":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Переговоры
        "Negotiation":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Торговля
        "Trade":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},
              }

    def __init__(self, name: str = "NoName", level: int = 1):
        self.name = name

        if (level <= 0) or (level == 1):
            self.level = 1
            self.experience = 0
            self.bounty = ADD_BOUNTY_FOR_FIRS_LEVEL
        else:
            self.level = level
            self.experience = (level - 1) * EXP_FOR_NEXT_LEVEL
            self.bounty = ADD_BOUNTY_FOR_FIRS_LEVEL + (self.level - 1) * ADD_BOUNTY_FOR_LEVEL

        self.dice = DICE_FOR_LEVEL[self.level]

    def __str__(self):
        return "Person name is " + self.name + " Level " + str(self.level) + " (experience " + str(self.experience) + ")"

    def cash_get(self):
        return self.cash

    def cash_set(self, value: float):
        self.cash = value

    def cash_change(self, value: float):
        self.cash += value

    def experience_get(self):
        return self.experience

    def experience_add(self, value: int):
        self.experience += value

        if self.level < (1 + (self.experience // EXP_FOR_NEXT_LEVEL)):
            tmp_lvl = (1 + (self.experience // EXP_FOR_NEXT_LEVEL)) - self.level
            self.level += tmp_lvl
            self.bounty += (ADD_BOUNTY_FOR_LEVEL * tmp_lvl)
            self.dice = DICE_FOR_LEVEL[self.level]

    def strength_get(self):
        return 1 + self.strength_bonus + self.strength_add

    def agility_get(self):
        return 1 + self.agility_bonus + self.agility_add

    def intellect_get(self):
        return 1 + self.intellect_bonus + self.intellect_add

    def initiative_get(self):
        return (self.initiative_bonus * FACTOR_INITIATIVE_BONUS) + \
               (self.initiative_add * FACTOR_INITIATIVE_ADD) + \
               + self.initiative_effect

    def health_get_all(self):
        return (self.health_bonus * FACTOR_HEALTH_BONUS) + \
               (self.health_add * FACTOR_HEALTH_ADD) + \
                self.health_effect

    def health_get_current(self):
        return self.health_current

    def energy_get_all(self):
        return (self.energy_bonus * FACTOR_ENERGY_BONUS) + \
               (self.energy_add * FACTOR_ENERGY_ADD) + \
                self.energy_effect

    def energy_get_current(self):
        return self.energy_current

    def persistence_get(self):
        return (self.persistence_bonus * FACTOR_ALL_RESISTENCES_BONUS) + \
               (self.persistence_add * FACTOR_ALL_RESISTENCES_ADD) + \
                self.persistence_effect

    def reaction_get(self):
        return (self.reaction_bonus * FACTOR_ALL_RESISTENCES_BONUS) + \
               (self.reaction_add * FACTOR_ALL_RESISTENCES_ADD) + \
                self.reaction_effect

    def consciousness__get(self):
        return (self.consciousness_bonus * FACTOR_ALL_RESISTENCES_BONUS) + \
               (self.consciousness_add * FACTOR_ALL_RESISTENCES_ADD) + \
                self.consciousness_effect

    def burden_get_all(self):
        return (self.burden_bonus * FACTOR_BURDEN_BONUS) + \
               (self.burden_add * FACTOR_BURDEN_ADD) + \
                self.burden_effect

    def burden_get_current(self):
        return self.burden_current

    def skill_get(self, skill_name: str):
        """
        Определяет и возвращает общий бонус по указанному Навыку
        :param skill_name: Наименование навыка
        :return: Общий бонус по указанному Навыку, или None, если Навык отсутствует
        """
        if self.skills.get(skill_name):
            bonus = self.skills[skill_name]["bonus"]
            add = self.skills[skill_name]["add"]
            effect = 0

            if len(self.skills[skill_name]["effect"]):
                for key, value in self.skills[skill_name]["effect"].items():
                    effect += value

            if self.skills[skill_name]["type"] == "strength":
                characteristic = self.strength_get()
            elif self.skills[skill_name]["type"] == "agility":
                characteristic = self.agility_get()
            elif self.skills[skill_name]["type"] == "intellect":
                characteristic = self.intellect_get()

            # Дополнительно включить type в расчет
            return \
                1 + (characteristic // 2) + \
                (bonus * FACTOR_ALL_RESISTENCES_BONUS) + \
                (add * FACTOR_ALL_RESISTENCES_ADD) + \
                 effect

        else: return None




test_pers = Person(level=1)
print(test_pers)
print(test_pers.bounty)
print("Dice = " + test_pers.dice)
print("="*25)
test_pers.experience_add(100)
print(test_pers)
print(test_pers.bounty)
print("Dice = " + test_pers.dice)
print("="*25)
print("skill_get(Medicine) = " + str(test_pers.skill_get("Medicine")))

# Написать метод повышения Характеристик, поднять через него Интеллект и проверить новый вывод skill_get(Medicine)