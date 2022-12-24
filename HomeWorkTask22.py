# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12
import random


def FillArray(len, arr):
    for _ in range(len):
        arr.append(random.randint(1, 10))
    return arr


n = int(input("Input array1 size: "))
m = int(input("Input array2 size: "))
array = []
array2 = []

ar = FillArray(n, array)
ar2 = FillArray(m, array2)
print(ar)
print(ar2)
print(end='Output: ')
print(n, m)
for i in set(ar):
    for j in set(ar2):
        if i == j:
            print(i, end=' ')
