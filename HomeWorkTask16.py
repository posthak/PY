# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

import random
n = int(input("Input array size N: "))
x = int(input("Input number X: "))
array = []
count = 0
for item in range(n):
    array.append(random.randint(1, n//2))
    if x == array[item]:
        count += 1

print(array)
print(f"Output: {count}")
