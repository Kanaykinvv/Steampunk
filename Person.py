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
        """
        Возвращает общее значение характеристики Сила,
        с учетом всех вложений
        :return: Общее значение характеристики Сила
        """
        return STRENGTH_START + self.strength_bonus + self.strength_add

    def strength_up(self, value: int = 1):
        """
        Повышение характеристики Сила
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:
            if self.level == 1:
                self.strength_bonus += value
            else:
                self.strength_add += value
            self.bounty -= value

    def agility_get(self):
        """
        Возвращает общее значение характеристики Ловкость,
        с учетом всех вложений
        :return: Общее значение характеристики Ловкость
        """
        return AGILITY_START + self.agility_bonus + self.agility_add

    def agility_up(self, value: int = 1):
        """
        Повышение характеристики Ловкость
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:
            if self.level == 1:
                self.agility_bonus += value
            else:
                self.agility_add += value
            self.bounty -= value

    def intellect_get(self):
        """
        Возвращает общее значение характеристики Интеллект,
        с учетом всех вложений
        :return: Общее значение характеристики Интеллект
        """
        return INTELLECT_START + self.intellect_bonus + self.intellect_add

    def intellect_up(self, value: int = 1):
        """
        Повышение характеристики Интеллект
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:
            if self.level == 1:
                self.intellect_bonus += value
            else:
                self.intellect_add += value
            self.bounty -= value

    def characteristic_up(self, characteristic: str, value: int = 1):
        """
        Повышение указанной характеристики
        :param characteristic: strength, agility, intellect
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:
            if characteristic == "strength":
                if self.level == 1:
                    self.intellect_bonus += value
                else:
                    self.intellect_add += value
            elif characteristic == "agility":
                if self.level == 1:
                    self.agility_bonus += value
                else:
                    self.agility_add += value
            elif characteristic == "intellect":
                if self.level == 1:
                    self.intellect_bonus += value
                else:
                    self.intellect_add += value
            self.bounty -= value

    def initiative_get(self):
        """
        Возвращает общее значение Инициативы
        :return: Общее значение Инициативы
        """
        result = FACTOR_INITIATIVE_START + \
                 round(self.agility_get() * FACTOR_INITIATIVE_AGILITY) + \
                (self.initiative_bonus * FACTOR_INITIATIVE_BONUS) + \
                (self.initiative_add * FACTOR_INITIATIVE_ADD) + \
                 self.initiative_effect

        if result < 0: result = 0

        return result

    def initiative_up(self, value: int = 1):
        """
        Повышение Инициативы
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:
            if self.level == 1:
                self.initiative_bonus += value
            else:
                self.initiative_add += value
            self.bounty -= value

    def health_get_all(self):
        """
        Возвращает общее значение Здоровья
        :return: Общее значение Здоровья
        """
        result = FACTOR_HEALTH_START + \
                 round(self.strength_get() * FACTOR_HEALTH_STRENGTH) + \
                 (self.health_bonus * FACTOR_HEALTH_BONUS) + \
                 (self.health_add * FACTOR_HEALTH_ADD) + \
                 self.health_effect

        if result <= 0: result = 1

        return result

    def health_get_current(self):
        """
        Возвращает текущее Здоровье
        :return: Текущее Здоровье
        """
        return self.health_current

    def energy_get_all(self):
        """
        Возвращает общее значение Энергии
        :return: Общее значение Энергии
        """
        result = FACTOR_ENERGY_START + \
                 round(self.strength_get() * FACTOR_ENERGY_STRENGTH) + \
                 (self.energy_bonus * FACTOR_ENERGY_BONUS) + \
                 (self.energy_add * FACTOR_ENERGY_ADD) + \
                  self.energy_effect

        if result < 0: result = 0

        return result

    def energy_get_current(self):
        """
        Возвращает текущую Энергию
        :return: Текущая Энергия
        """
        return self.energy_current

    def persistence_get(self):
        """
        Возвращает значение Стойкости
        :return: Значение Стойкости
        """
        result = round(self.strength_get() * FACTOR_ALL_RESISTENCES_CHAR) + \
                 (self.persistence_bonus * FACTOR_ALL_RESISTENCES_BONUS) + \
                 (self.persistence_add * FACTOR_ALL_RESISTENCES_ADD) + \
                  self.persistence_effect

        if result < 0: result = 0

        return result

    def persistence_up(self, value: int = 1):
        """
        Увеличение параметра Стойкости
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:
            if self.level == 1:
                self.persistence_bonus += value
            else:
                self.persistence_add += value
            self.bounty -= value

    def reaction_get(self):
        """
        Возвращает значение Реакции
        :return: Значение Реакции
        """
        result = round(self.agility_get() * FACTOR_ALL_RESISTENCES_CHAR) + \
                 (self.reaction_bonus * FACTOR_ALL_RESISTENCES_BONUS) + \
                 (self.reaction_add * FACTOR_ALL_RESISTENCES_ADD) + \
                 self.reaction_effect

        if result < 0: result = 0

        return result

    def reaction_up(self, value: int = 1):
        """
        Увеличение параметра Реакции
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:
            if self.level == 1:
                self.reaction_bonus += value
            else:
                self.reaction_add += value
            self.bounty -= value

    def consciousness_get(self):
        """
        Возвращает значение Сознания
        :return: Значение Сознания
        """
        result = round(self.intellect_get() * FACTOR_ALL_RESISTENCES_CHAR) + \
                 (self.consciousness_bonus * FACTOR_ALL_RESISTENCES_BONUS) + \
                 (self.consciousness_add * FACTOR_ALL_RESISTENCES_ADD) + \
                 self.consciousness_effect

        if result < 0: result = 0

        return result

    def consciousness_up(self, value: int = 1):
        """
        Увеличение параметра Сознания
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:
            if self.level == 1:
                self.consciousness_bonus += value
            else:
                self.consciousness_add += value
            self.bounty -= value

    def burden_get_all(self):
        """
        Возвращает максимально возможный вес ноши, если это значение меньше 0 (ввиду эффекта), то
        максимальный вес будет равен 0.
        :return: Возвращает максимально возможный вес ноши.
        """
        result = FACTOR_BURDEN_START + \
                 (self.strength_get() * FACTOR_BURDEN_STRENGTH) + \
                 (self.burden_bonus * FACTOR_BURDEN_BONUS) + \
                 (self.burden_add * FACTOR_BURDEN_ADD) + \
                  self.burden_effect

        if result < 0: result = 0

        return result

    def burden_get_current(self):
        """
        Возвращает текущий вес ноши
        :return: Текущий вес ноши
        """
        # Необходимо тут проводить считывание всего перечня переносимых вещей
        return self.burden_current

    def burden_up(self, value: int = 1):
        """
        Увеличение параметра максимальной ноши
        :return:
        """
        if self.bounty >= value:
            if self.level == 1:
                self.burden_bonus += value
            else:
                self.burden_add += value
            self.bounty -= value

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

    def skill_up(self, skill_name: str, value: int = 1):
        """
        Повышение выбранного Навыка на указанное значение
        :param skill_name: Наименование Навыка
        :param value: Значение, на которое необходимо увеличить Навык
        :return:
        """
        if (self.bounty >= value) and (self.skills.get(skill_name)):
            if self.level == 1:
                self.skills[skill_name]["bonus"] += value
            else:
                self.skills[skill_name]["add"] += value
            self.bounty -= value



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
test_pers.intellect_up(5)
print("skill_get(Medicine) = " + str(test_pers.skill_get("Medicine")))
print("="*25)
print("skill_get(HeavyWeapon) = " + str(test_pers.skill_get("HeavyWeapon")))
test_pers.strength_up(1)
print("skill_get(HeavyWeapon) = " + str(test_pers.skill_get("HeavyWeapon")))
print("="*25)
print("burden_get_all = " + str(test_pers.burden_get_all()))
