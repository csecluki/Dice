import random
import matplotlib.pyplot as plt


class Dice:

    def __init__(self):
        self.min = 1
        self.max = 6

    def roll(self):
        return int(random.randrange(self.min, self.max + 1))


class Roll:

    def __init__(self, first_dice, second_dice):
        self.a = first_dice
        self.b = second_dice

    def __call__(self):
        return self.a.roll() + self.b.roll()


dice1 = Dice()
dice2 = Dice()
roll = Roll(dice1, dice2)
overall_register = [0 for n in range(13)]
games = 100

min_2, min_7, min_12 = 10000, 1000, 1000
max_2, max_7, max_12 = 0, 0, 0
count_min_2, count_max_2, count_min_7, count_max_7, count_min_12, count_max_12 = 0, 0, 0, 0, 0, 0

for i in range(games):
    register = [0 for n in range(13)]
    for j in range(80):
        register[roll()] += 1

    # print(register[2:])

    if register[2] < min_2:
        min_2 = register[2]
        count_min_2 = 1
    elif register[2] == min_2:
        count_min_2 += 1

    if register[2] > max_2:
        max_2 = register[2]
        count_max_2 = 1
    elif register[2] == max_2:
        count_max_2 += 1

    if register[7] < min_7:
        min_7 = register[7]
        count_min_7 = 1
    elif register[7] == min_7:
        count_min_7 += 1

    if register[7] > max_7:
        max_7 = register[7]
        count_max_7 = 1
    elif register[7] == max_7:
        count_max_7 += 1

    if register[-1] < min_12:
        min_12 = register[-1]
        count_min_12 = 1
    elif register[-1] == min_12:
        count_min_12 += 1

    if register[-1] > max_12:
        max_12 = register[-1]
        count_max_12 = 1
    elif register[-1] == max_12:
        count_max_12 += 1

    for k in range(len(register)):
        overall_register[k] += register[k]

print()
print(f"Minimum number of 2s rolled in game: {min_2}, number of these games: {count_min_2}")
print(f"Maximum number of 2s rolled in game: {max_2}, number of these games: {count_max_2}")
print()

print(f"Minimum number of 7s rolled in game: {min_7}, number of these games: {count_min_7}")
print(f"Maximum number of 7s rolled in game: {max_7}, number of these games: {count_max_7}")
print()

print(f"Minimum number of 12s rolled in game: {min_12}, number of these games: {count_min_12}")
print(f"Maximum number of 12s rolled in game: {max_12}, number of these games: {count_max_12}")
print()

print(overall_register[2:])

chart = plt.figure()
ax = chart.add_axes([0, 0, 1, 1])
x_cor = [i for i in range(2, 13)]
y_cor = overall_register[2:]
ax.bar(x_cor, y_cor)
plt.show()
