# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6


import random
n = int(input("Input array size N: "))
x = int(input("Input number X: "))
array = []
array2 = []
res = 0
for item in range(n):
    array.append(random.randint(1, n))
    array2.append(x - array[item])

min = n
array2.sort(reverse=True)
for k in range(n):
    if min > abs(array2[k]) > 0:
        min = abs(array2[k])
        res = array2[k]
print(array)
print(x-res)
