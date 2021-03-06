
ADD_BOUNTY_FOR_FIRS_LEVEL = 10      # Количество очков развития, выдаваемое на первом уровне (при создании)
ADD_BOUNTY_FOR_LEVEL = 1            # Количество очков развития, выдаваемое за уровень

EXP_FOR_NEXT_LEVEL = 10             # Количество опыта для перехода на следующий уровень

DICE_FOR_LEVEL = {                  # Тип и количество игровых кубиков в зависимости от уровня
                    1: "1d4",
                    2: "1d4",
                    3: "1d6",
                    4: "1d6",
                    5: "1d6",
                    6: "1d8",
                    7: "1d8",
                    8: "1d8",
                    9: "1d8",
                    10: "2d4",
                    11: "2d4",
                    12: "2d4",
                    13: "2d4",
                    14: "2d4",
                    15: "1d10",
                    16: "1d10",
                    17: "1d10",
                    18: "1d10",
                    19: "1d10",
                    20: "1d10",
                    21: "1d12",
                    22: "1d12",
                    23: "1d12",
                    24: "1d12",
                    25: "1d12",
                    26: "1d12",
                    27: "1d12",
                    28: "2d6",
                    29: "2d6",
                    30: "2d6",
                    31: "2d6",
                    32: "2d6",
                    33: "2d6",
                    34: "2d6",
                    35: "2d6",
                    36: "2d8",
                    37: "2d8",
                    38: "2d8",
                    39: "2d8",
                    40: "2d8",
                    41: "2d8",
                    42: "2d8",
                    43: "2d8",
                    44: "2d8",
                    45: "1d20",
                    46: "1d20",
                    47: "1d20",
                    48: "1d20",
                    49: "1d20",
                    50: "1d20",
                    51: "1d20",
                    52: "1d20",
                    53: "1d20",
                    54: "1d20",
                    55: "2d10",
                    56: "2d10",
                    57: "2d10",
                    58: "2d10",
                    59: "2d10",
                    60: "2d10",
                    61: "2d10",
                    62: "2d10",
                    63: "2d10",
                    64: "2d10",
                    65: "2d10",
                    66: "2d12",
                    67: "2d12",
                    68: "2d12",
                    69: "2d12",
                    70: "2d12",
                    71: "2d12",
                    72: "2d12",
                    73: "2d12",
                    74: "2d12",
                    75: "2d12",
                    76: "2d12",
                    77: "2d12",
                    78: "2d20",
                    79: "2d20",
                    80: "2d20",
                    81: "2d20",
                    82: "2d20",
                    83: "2d20",
                    84: "2d20",
                    85: "2d20",
                    86: "2d20",
                    87: "2d20",
                    88: "2d20",
                    89: "2d20",
                    90: "2d20",
                    91: "3d20",
                    92: "3d20",
                    93: "3d20",
                    94: "3d20",
                    95: "3d20",
                    96: "3d20",
                    97: "3d20",
                    98: "3d20",
                    99: "3d20",
                    100: "3d20"
}
STRENGTH_START = 1                  # Сила (стартовое значение)
AGILITY_START = 1                   # Ловкость (стартовое значение)
INTELLECT_START = 1                 # Интеллект (стартовое значение)

FACTOR_INITIATIVE_BONUS = 5         # Инициатива (бонус)
FACTOR_INITIATIVE_ADD = 3           # Инициатива (улучшение)
FACTOR_INITIATIVE_AGILITY = 1.25    # Инициатива (индекс по Ловкости)
FACTOR_INITIATIVE_START = 1         # Инициатива (стартовое значение)

FACTOR_HEALTH_BONUS = 17            # Здоровье (бонус)
FACTOR_HEALTH_ADD = 10              # Здоровье (улучшение)
FACTOR_HEALTH_STRENGTH = 4          # Здоровье (индекс по Силе)
FACTOR_HEALTH_START = 8             # Здоровье (стартовое значение)

FACTOR_ENERGY_BONUS = 8             # Энергия (бонус)
FACTOR_ENERGY_ADD = 5               # Энергия (улучшение)
FACTOR_ENERGY_STRENGTH = 2          # Энергия (индекс по Силе)
FACTOR_ENERGY_START = 4             # Энергия (стартовое значение)

FACTOR_ALL_RESISTENCES_BONUS = 3    # Все сопростивления (бонус)
FACTOR_ALL_RESISTENCES_ADD = 2      # Все сопростивления (улучшение)
FACTOR_ALL_RESISTENCES_CHAR = 0.5   # Все сопростивления (индекс по характеристике)

FACTOR_BURDEN_BONUS = 42            # Ноша (бонус)
FACTOR_BURDEN_ADD = 25              # Ноша (улучшение)
FACTOR_BURDEN_STRENGTH = 12         # Ноша (индекс по Силе)
FACTOR_BURDEN_START = 24            # Ноша (стартовое значение)

FACTOR_ALL_SKILLS_BONUS = 3         # Все навыки (бонус)
FACTOR_ALL_SKILLS_ADD = 2           # Все навыки (улучшение)
