# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input("Input first number: "))
b = int(input("Input second number: "))


def GetSum(a, b):
    if b == 0:
        return a
    else:
        return GetSum(a+1, b-1)


print(GetSum(a, b))
