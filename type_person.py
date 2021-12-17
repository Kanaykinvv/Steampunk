import random
# Указаны типы персонажей и их возможные параметры

# Warrior = {
#     "strength"      : 0,
#     "agility"       : 0,
#     "intellect"     : 0,
#     "initiative"    : 0,
#     "health"        : 0,
#     "energy"        : 0,
#     "persistence"   : 0,
#     "reaction"      : 0,
#     "consciousness" : 0,
#     "burden"        : 0,
# }
Warrior = {
    "strength"      : 30,
    "agility"       : 30,
    "intellect"     : 0,
}

max = 0

tmp = {k: v for k, v in sorted(Warrior.items(), key=lambda item: item[1], reverse=True)}
print(tmp)


for value in Warrior.values():
    max += value

chance = random.randrange(0, max, 1)
print("Range = 0 - " + str(max))
print("chance = " + str(chance))

current_chance = 0
current_key = ""
for key, value in Warrior.items():
    current_chance += value
    if chance < current_chance:
        current_key = key
        break

print("current_chance = " + str(current_chance))
print("current_key = " + str(current_key))