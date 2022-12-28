# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


a = int(input("Input number: "))
b = int(input("Input power: "))


def GetPower(a, b):
    if b == 1:
        return a
    else:
        return a * GetPower(a, b-1)


print(GetPower(a, b))
