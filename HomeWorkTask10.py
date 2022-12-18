# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random


def GetMinCoins():
    array = []
    n = 5
    sum = 0
    for item in range(n):
        array.append(random.randint(0, 1))
        sum += array[item]

    if sum < n/2:
        print(f"{n} -> {array}")
        print(sum)
    else:
        print(f"{n} -> {array}")
        print(n-sum)


GetMinCoins()
