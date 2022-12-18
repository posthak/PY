# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def GetPowNum(num):
    m = 1
    print(num, end=' -> ')
    while m <= num:
        print(m, end=' ')
        m *= 2


n = int(input('Input number N: '))
GetPowNum(n)
