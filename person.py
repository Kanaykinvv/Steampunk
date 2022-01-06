import datetime
import random
import items
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
        "athletics":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Без оружия
        "no_weapons":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Выносливость
        "endurance":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Метание
        "throwing":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Тяжёлое оружие
        "heavy_weapon":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Холодное оружие
        "cold_weapon":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "strength"},

        # Навык - Азартные игры
        "gambl":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Акробатика
        "acrobatics":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Воровство
        "theft":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Лёгкое оружие
        "light_weapon":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Ловушки
        "traps":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Наблюдательность
        "observation":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "agility"},

        # Навык - Взлом
        "hack":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Высокотехнологичное оружие
        "hightech_weapons":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Инженерия
        "engineering":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Медицина
        "medicine":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Переговоры
        "negotiation":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},

        # Навык - Торговля
        "trade":
            {"bonus": 0,
             "add": 0,
             "effect": {},
             "type": "intellect"},
              }

    # Хронология прокачки персонажа
    update_log = []

    def update_log_add(self, message: str):
        self.update_log.append([datetime.datetime.now(), message])

    def update_log_print(self):
        for unit in self.update_log:
            print(str(unit[0]).ljust(10) + unit[1])

    def cash_get(self):
        """
        Получить текущее количество валюты
        :return: Текущее количество валюты
        """
        return self.cash

    def cash_set(self, value: float):
        """
        Установить количество валюты на указанное число
        :param value: Количество валюты
        :return:
        """
        self.cash = value
        self.update_log_add("[cash_set]".ljust(20) + str(value))

    def cash_change(self, value: float):
        """
        Изменение количества валюты
        :param value: Количество валюты
        :return: -
        """
        self.cash += value
        self.update_log_add("[cash_change]".ljust(20) + str(value))

    def experience_get(self):
        """
        Текущее колчество опыта
        :return: Текущее колчество опыта
        """
        return self.experience

    def experience_add(self, value: int):
        """
        Увеличение опыта
        :param value: Количество полученного опыта
        :return: -
        """
        self.experience += value
        self.update_log_add("[experience_add]".ljust(20) + str(value))

        if self.level < (1 + (self.experience // EXP_FOR_NEXT_LEVEL)):
            tmp_lvl = (1 + (self.experience // EXP_FOR_NEXT_LEVEL)) - self.level
            self.level += tmp_lvl
            self.bounty += (ADD_BOUNTY_FOR_LEVEL * tmp_lvl)
            self.dice = DICE_FOR_LEVEL[self.level]
            self.update_log_add("[experience_add]".ljust(20) + "Level up!")
            self.update_log_add("[experience_add]".ljust(20) + "level = " + str(self.level))
            self.update_log_add("[experience_add]".ljust(20) + "bounty = " + str(self.bounty))
            self.update_log_add("[experience_add]".ljust(20) + "dice = " + str(self.dice))

    def strength_get(self):
        """
        Возвращает общее значение характеристики Сила,
        с учетом всех вложений
        :return: Общее значение характеристики Сила
        """
        return STRENGTH_START + self.strength_bonus + self.strength_add

    def strength_up(self, value: int = 1):
        """
        Повышение характеристики Сила (с учетом повышения Здоровья и Энергии)
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:

            health_diff_current = self.health_get_all() - self.health_get_current()
            energy_diff_current = self.energy_get_all() - self.energy_get_current()

            if self.level == 1:
                self.strength_bonus += value
            else:
                self.strength_add += value
            self.bounty -= value

            self.health_current = self.health_get_all() - health_diff_current
            self.energy_current = self.energy_get_all() - energy_diff_current

            self.update_log_add("[strength_up]".ljust(20) + str(value))

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

            self.update_log_add("[agility_up]".ljust(20) + str(value))

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

            self.update_log_add("[intellect_up]".ljust(20) + str(value))

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

            self.update_log_add("[initiative_up]".ljust(20) + str(value))

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

    def health_up(self, value: int = 1):
        """
        Увеличение параметра Здоровье
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:

            health_diff_current = self.health_get_all() - self.health_get_current()

            if self.level == 1:
                self.health_bonus += value
            else:
                self.health_add += value

            self.bounty -= value
            self.health_current = self.health_get_all() - health_diff_current

            self.update_log_add("[health_up]".ljust(20) + str(value))


    def health_change(self, value: int):
        """
        Изменение параметра Здоровье
        :param value: Значение изменения
        :return: -
        """
        if self.health_current + value < 0:
            self.health_current = 0
        else:
            self.health_current += value

        self.update_log_add("[health_change]".ljust(20) + str(value))

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

    def energy_up(self, value: int = 1):
        """
        Увеличение параметра Энергия
        :param value: Значение увеличения
        :return: -
        """
        if self.bounty >= value:
            energy_diff_current = self.energy_get_all() - self.energy_get_current()

            if self.level == 1:
                self.energy_bonus += value
            else:
                self.energy_add += value
            self.bounty -= value
            self.energy_current = self.energy_get_all() - energy_diff_current
            self.update_log_add("[energy_up]".ljust(20) + str(value))

    def energy_change(self, value: int):
        """
        Изменение параметра Энергия
        :param value: Значение изменения
        :return: -
        """
        if self.energy_current + value < 0:
            self.energy_current = 0
        else:
            self.energy_current += value

        self.update_log_add("[energy_change]".ljust(20) + str(value))

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

            self.update_log_add("[persistence_up]".ljust(20) + str(value))

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

            self.update_log_add("[reaction_up]".ljust(20) + str(value))

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

            self.update_log_add("[consciousness_up]".ljust(20) + str(value))

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
        result = 0.0
        for key in self.equipment:
            result += self.equipment[key] * items.ITEMS[key]["weight"]
        self.burden_current = result
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

            self.update_log_add("[burden_up]".ljust(20) + str(value))

    def skill_get(self, skill_name: str):
        """
        Определяет и возвращает общий бонус по указанному Навыку
        :param skill_name: Наименование навыка
            "athletics"                 # Навык - Атлетика
            "no_weapons"                # Навык - Без оружия
            "endurance"                 # Навык - Выносливость
            "throwing"                  # Навык - Метание
            "heavy_weapon"              # Навык - Тяжёлое оружие
            "cold_weapon"               # Навык - Холодное оружие
            "gambl"                     # Навык - Азартные игры
            "acrobatics"                # Навык - Акробатика
            "theft"                     # Навык - Воровство
            "light_weapon"              # Навык - Лёгкое оружие
            "traps"                     # Навык - Ловушки
            "observation"               # Навык - Наблюдательность
            "hack"                      # Навык - Взлом
            "hightech_weapons"          # Навык - Высокотехнологичное оружие
            "engineering"               # Навык - Инженерия
            "medicine"                  # Навык - Медицина
            "negotiation"               # Навык - Переговоры
            "trade"                     # Навык - Торговля
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

            self.update_log_add("[skill_up] [" + skill_name + "]".ljust(20) + str(value))

    def equipment_add(self, name: str, count: int = 1):
        """
        Добавление предмета в инвентарь, если есть свободный вес (ноша)
        :param name: Наименование предмета
        :param count: Количество предметов
        :return: -
        """
        if name in items.ITEMS.keys():
            if (self.burden_get_all() - self.burden_current) >= items.ITEMS["name"]["weight"]:
                if name in self.equipment:
                    self.equipment[name] += count
                else: self.equipment[name] = count

                self.burden_get_current()
            else:
                print("Нет столько свободного веса!")
        else:
            print("Нет такого предмета!")

    def equipment_del(self, name: str):
        """
        Удаление предмета из инвентаря
        :param name: Наименование предмета
        :return: -
        """
        if name in self.equipment:
            del self.equipment[name]
            self.burden_get_current()

    def equipment_use(self, name: str, count: int = 1):
        """
        Использование предмета из инвентаря
        :param name: Наименование предмета
        :param count: Количество использованных предметов
        :return: -
        """
        if (name in self.equipment) and (self.equipment[name] >= count):
            self.equipment[name] -= count
            if self.equipment[name] == 0:
                self.equipment_del(name)
            self.burden_get_current()

    def parameter_up(self, name: str, value: int = 1):
        """
        Повышение любого параметра на указанную величину (по умолчанию на 1)
        :param name: Наименование параметра.
        Принимает значение:
            "strength"                  # Сила
            "agility"                   # Ловкость
            "intellect"                 # Интеллект
            "initiative"                # Инициатива
            "health"                    # Здоровье
            "energy"                    # Энергия
            "persistence"               # Стойкость
            "reaction"                  # Реакция
            "consciousness"             # Сознание
            "burden"                    # Ноша
            "athletics"                 # Навык - Атлетика
            "no_weapons"                # Навык - Без оружия
            "endurance"                 # Навык - Выносливость
            "throwing"                  # Навык - Метание
            "heavy_weapon"              # Навык - Тяжёлое оружие
            "cold_weapon"               # Навык - Холодное оружие
            "gambl"                     # Навык - Азартные игры
            "acrobatics"                # Навык - Акробатика
            "theft"                     # Навык - Воровство
            "light_weapon"              # Навык - Лёгкое оружие
            "traps"                     # Навык - Ловушки
            "observation"               # Навык - Наблюдательность
            "hack"                      # Навык - Взлом
            "hightech_weapons"          # Навык - Высокотехнологичное оружие
            "engineering"               # Навык - Инженерия
            "medicine"                  # Навык - Медицина
            "negotiation"               # Навык - Переговоры
            "trade"                     # Навык - Торговля
        :param value: Значение, на которое необходимо увеличить указанный параметр
        :return: -
        """
        if name == "strength":
            self.strength_up(value)
        elif name == "agility":
            self.agility_up(value)
        elif name == "intellect":
            self.intellect_up(value)
        elif name == "initiative":
            self.initiative_up(value)
        elif name == "health":
            self.health_up(value)
        elif name == "energy":
            self.energy_up(value)
        elif name == "persistence":
            self.persistence_up(value)
        elif name == "reaction":
            self.reaction_up(value)
        elif name == "consciousness":
            self.consciousness_up(value)
        elif name == "burden":
            self.burden_up(value)
        elif name == "athletics":
            self.skill_up("athletics", value)
        elif name == "no_weapons":
            self.skill_up("no_weapons", value)
        elif name == "endurance":
            self.skill_up("endurance", value)
        elif name == "throwing":
            self.skill_up("throwing", value)
        elif name == "heavy_weapon":
            self.skill_up("heavy_weapon", value)
        elif name == "cold_weapon":
            self.skill_up("cold_weapon", value)
        elif name == "gambl":
            self.skill_up("gambl", value)
        elif name == "acrobatics":
            self.skill_up("acrobatics", value)
        elif name == "theft":
            self.skill_up("theft", value)
        elif name == "light_weapon":
            self.skill_up("light_weapon", value)
        elif name == "traps":
            self.skill_up("traps", value)
        elif name == "observation":
            self.skill_up("observation", value)
        elif name == "hack":
            self.skill_up("hack", value)
        elif name == "hightech_weapons":
            self.skill_up("hightech_weapons", value)
        elif name == "engineering":
            self.skill_up("engineering", value)
        elif name == "medicine":
            self.skill_up("medicine", value)
        elif name == "negotiation":
            self.skill_up("negotiation", value)
        elif name == "trade":
            self.skill_up("trade", value)

    def __init__(self, name: str = "NoName", level: int = 1):
        """
        Инициализация класса, определение опыта и дайса, исходя из уровня.
        Установка значения Здоровья и Энергии.
        :param name: Имя персонажа
        :param level: Уровень персонажа
        """
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
        self.health_current = self.health_get_all()
        self.energy_current = self.energy_get_all()

    def __str__(self):
        """
        Печать текущего класса
        :return: Вывод имени, уровня и опыта
        """
        result = "="*50 + "\n" + \
                 "ОСНОВНАЯ ИНФОРМАЦИЯ".center(50, " ") + "\n" + \
                 "=" * 50 + "\n" + \
                 "Имя персонажа: ".ljust(30, " ") + self.name + "\n" + \
                 "Текущий уровень: ".ljust(30, " ") + str(self.level) + "\n" + \
                 "Количество текущего опыта: ".ljust(30, " ") + str(self.experience_get()) + "\n" + \
                 "Количество денежных средств: ".ljust(30, " ") + str(self.cash_get()) + "\n" + \
                 "Текущий кубик: ".ljust(30, " ") + self.dice + "\n" + \
                 "Текущие очки развития: ".ljust(30, " ") + str(self.bounty) + "\n" + \
                 "=" * 50 + "\n" + \
                 "ХАРАКТЕРИСТИКИ".center(50, " ") + "\n" + \
                 "=" * 50 + "\n" + \
                 "Сила ".ljust(30, " ") + str(self.strength_get()) + "\n" + \
                 "Ловкость ".ljust(30, " ") + str(self.agility_get()) + "\n" + \
                 "Интеллект ".ljust(30, " ") + str(self.intellect_get()) + "\n" + \
                 "=" * 50 + "\n" + \
                 "Здоровье ".ljust(30, " ") + str(self.health_get_current()) + " / " + str(self.health_get_all()) + "\n" + \
                 "Энергия ".ljust(30, " ") + str(self.energy_get_current()) + " / " + str(self.energy_get_all()) + "\n" + \
                 "-" * 50 + "\n" + \
                 "Инициатива ".ljust(30, " ") + str(self.initiative_get()) + "\n" + \
                 "Стойкость ".ljust(30, " ") + str(self.persistence_get()) + "\n" + \
                 "Реакция ".ljust(30, " ") + str(self.reaction_get()) + "\n" + \
                 "Сознание ".ljust(30, " ") + str(self.consciousness_get()) + "\n" + \
                 "Ноша ".ljust(30, " ") + str(self.burden_get_current()) + " / " + str(self.burden_get_all()) + "\n" + \
                 "=" * 50 + "\n" + \
                 "НАВЫКИ".center(50, " ") + "\n" + \
                 "=" * 50 + "\n" + \
                 "Навык - Атлетика ".ljust(48, "·") + " " + str(self.skill_get("athletics")) + "\n" + \
                 "Навык - Без оружия ".ljust(48, "·") + " " + str(self.skill_get("no_weapons")) + "\n" + \
                 "Навык - Выносливость ".ljust(48, "·") + " " + str(self.skill_get("endurance")) + "\n" + \
                 "Навык - Метание ".ljust(48, "·") + " " + str(self.skill_get("throwing")) + "\n" + \
                 "Навык - Тяжёлое оружие ".ljust(48, "·") + " " + str(self.skill_get("heavy_weapon")) + "\n" + \
                 "Навык - Холодное оружие ".ljust(48, "·") + " " + str(self.skill_get("cold_weapon")) + "\n" + \
                 "-" * 50 + "\n" + \
                 "Навык - Азартные игры ".ljust(48, "·") + " " + str(self.skill_get("gambl")) + "\n" + \
                 "Навык - Акробатика ".ljust(48, "·") + " " + str(self.skill_get("acrobatics")) + "\n" + \
                 "Навык - Воровство ".ljust(48, "·") + " " + str(self.skill_get("theft")) + "\n" + \
                 "Навык - Лёгкое оружие ".ljust(48, "·") + " " + str(self.skill_get("light_weapon")) + "\n" + \
                 "Навык - Ловушки ".ljust(48, "·") + " " + str(self.skill_get("traps")) + "\n" + \
                 "Навык - Наблюдательность ".ljust(48, "·") + " " + str(self.skill_get("observation")) + "\n" + \
                 "-" * 50 + "\n" + \
                 "Навык - Взлом ".ljust(48, "·") + " " + str(self.skill_get("hack")) + "\n" + \
                 "Навык - Высокотехнологичное оружие ".ljust(48, "·") + " " + str(self.skill_get("hightech_weapons")) + "\n" + \
                 "Навык - Инженерия ".ljust(48, "·") + " " + str(self.skill_get("engineering")) + "\n" + \
                 "Навык - Медицина ".ljust(48, "·") + " " + str(self.skill_get("medicine")) + "\n" + \
                 "Навык - Переговоры ".ljust(48, "·") + " " + str(self.skill_get("negotiation")) + "\n" + \
                 "Навык - Торговля ".ljust(48, "·") + " " + str(self.skill_get("trade")) + "\n" + \
                 "-" * 50 + "\n" + \
                 "ЭКИПИРОВКА".center(50, " ") + "\n" + \
                 "-" * 50 + "\n"

        equipment = ""
        for item in self.equipment:
            equipment += item.ljust(48, "·") + " " + str(self.equipment[item]) + "\n"

        return result + equipment

    # Проблемы:
    # - Перерсчет всех показателей при добавлении/исключении Эффектов

# Указаны типы персонажей и их возможные параметры
types = {
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

def create_items(person: Person, burden_max: int = 20):
    # Количество денег
    a = random.randint(0, person.level)
    b = random.randint(0, burden_max)
    generate_cash = int(a * b * (random.randint(1, 11) / 10))
    person.cash_change(generate_cash)

    tmp_burden = int((person.burden_get_current() / person.burden_get_all()) * 100)
    print("Текущий процент загруженности: " + str(tmp_burden) + " | текущий вес: " + str(person.burden_get_current()))

    while tmp_burden <= burden_max:
        if int(( ( items.ITEMS["name"]["weight"] + person.burden_get_current()) / person.burden_get_all()) * 100) <= burden_max:
            person.equipment_add("name", 1)
            tmp_burden = int((person.burden_get_current() / person.burden_get_all()) * 100)
            print("Текущий процент загруженности: " + str(tmp_burden) + " | текущий вес: " + str(person.burden_get_current()))
        else:
            break

def create_person(type: str, level: int = 1):

    if type in types:
        person = Person(name="MyPers_1", level=level)

        parameter_priority = {k: v for k, v in sorted(types[type].items(),
                                                      key=lambda item: item[1],
                                                      reverse=True)}
        # Указано для теста проверки сортировки
        #print(parameter_priority)

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




# Tests
my_test_person = create_person(type="warrior", level=15)
create_items(my_test_person)
print(my_test_person)
my_test_person.update_log_print()

# test_pers = Person(level=2)
# test_pers.equipment_add(name="name", count=1)
# print(test_pers)


