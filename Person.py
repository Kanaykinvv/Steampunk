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

    skill_Athletics_bonus = 0           # Навык - Атлетика (бонус)
    skill_Athletics_effect = 0          # Навык - Атлетика (эффект)
    skill_Athletics_add = 0             # Навык - Атлетика (улучшение)

    skill_NoWeapons_bonus = 0           # Навык - Без оружия (бонус)
    skill_NoWeapons_effect = 0          # Навык - Без оружия (эффект)
    skill_NoWeapons_add = 0             # Навык - Без оружия (улучшение)

    skill_Endurance_bonus = 0           # Навык - Выносливость (бонус)
    skill_Endurance_effect = 0          # Навык - Выносливость (эффект)
    skill_Endurance_add = 0             # Навык - Выносливость (улучшение)

    skill_Throwing_bonus = 0            # Навык - Метание (бонус)
    skill_Throwing_effect = 0           # Навык - Метание (эффект)
    skill_Throwing_add = 0              # Навык - Метание (улучшение)

    skill_HeavyWeapon_bonus = 0         # Навык - Тяжёлое оружие (бонус)
    skill_HeavyWeapon_effect = 0        # Навык - Тяжёлое оружие (эффект)
    skill_HeavyWeapon_add = 0           # Навык - Тяжёлое оружие (улучшение)

    skill_ColdWeapon_bonus = 0          # Навык - Холодное оружие (бонус)
    skill_ColdWeapon_effect = 0         # Навык - Холодное оружие (эффект)
    skill_ColdWeapon_add = 0            # Навык - Холодное оружие (улучшение)

    skill_Gambl_bonus = 0               # Навык - Азартные игры (бонус)
    skill_Gambl_effect = 0              # Навык - Азартные игры (эффект)
    skill_Gambl_add = 0                 # Навык - Азартные игры (улучшение)

    skill_Acrobatics_bonus = 0          # Навык - Акробатика (бонус)
    skill_Acrobatics_effect = 0         # Навык - Акробатика (эффект)
    skill_Acrobatics_add = 0            # Навык - Акробатика (улучшение)

    skill_Theft_bonus = 0               # Навык - Воровство (бонус)
    skill_Theft_effect = 0              # Навык - Воровство (эффект)
    skill_Theft_add = 0                 # Навык - Воровство (улучшение)

    skill_LightWeapon_bonus = 0         # Навык - Лёгкое оружие (бонус)
    skill_LightWeapon_effect = 0        # Навык - Лёгкое оружие (эффект)
    skill_LightWeapon_add = 0           # Навык - Лёгкое оружие (улучшение)

    skill_Traps_bonus = 0               # Навык - Ловушки (бонус)
    skill_Traps_effect = 0              # Навык - Ловушки (эффект)
    skill_Traps_add = 0                 # Навык - Ловушки (улучшение)

    skill_Observation_bonus = 0         # Навык - Наблюдательность (бонус)
    skill_Observation_effect = 0        # Навык - Наблюдательность (эффект)
    skill_Observation_add = 0           # Навык - Наблюдательность (улучшение)

    skill_Hack_bonus = 0                # Навык - Взлом (бонус)
    skill_Hack_effect = 0               # Навык - Взлом (эффект)
    skill_Hack_add = 0                  # Навык - Взлом (улучшение)

    skill_HightechWeapons_bonus = 0     # Навык - Высокотехнологичное оружие (бонус)
    skill_HightechWeapons_effect = 0    # Навык - Высокотехнологичное оружие (эффект)
    skill_HightechWeapons_add = 0       # Навык - Высокотехнологичное оружие (улучшение)

    skill_Engineering_bonus = 0         # Навык - Инженерия (бонус)
    skill_Engineering_effect = 0        # Навык - Инженерия (эффект)
    skill_Engineering_add = 0           # Навык - Инженерия (улучшение)

    skill_Medicine_bonus = 0            # Навык - Медицина (бонус)
    skill_Medicine_effect = 0           # Навык - Медицина (эффект)
    skill_Medicine_add = 0              # Навык - Медицина (улучшение)

    skill_Negotiation_bonus = 0         # Навык - Переговоры (бонус)
    skill_Negotiation_effect = 0        # Навык - Переговоры (эффект)
    skill_Negotiation_add = 0           # Навык - Переговоры (улучшение)

    skill_Trade_bonus = 0               # Навык - Торговля (бонус)
    skill_Trade_effect = 0              # Навык - Торговля (эффект)
    skill_Trade_add = 0                 # Навык - Торговля (улучшение)

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


test_pers = Person(level=1)
print(test_pers)
print(test_pers.bounty)
print("Dice = " + test_pers.dice)
print("="*25)
test_pers.experience_add(100)
print(test_pers)
print(test_pers.bounty)
print("Dice = " + test_pers.dice)