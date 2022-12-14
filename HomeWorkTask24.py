# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Input: 4
# (значения сгенерированы случайным образом
#  4 2 3 1)
# Output: 9
import random
import json


def FillArray(len, arr):
    for _ in range(len):
        arr.append(random.randint(1, 5))
    return arr


def WriteToFile(arr):
    data = open('file.txt', 'w')
    data.writelines(str(arr))
    data.close()


def ReadFormFile():
    path = 'file.txt'
    data = open(path, 'r')
    # ar = data.readlines()
    ar = json.load(data)
    data.close()
    return ar


n = int(input("Input the quantity of bushes: "))
array = []
WriteToFile(FillArray(n, array))
resArray = ReadFormFile()

max = resArray[-1]+resArray[0] + resArray[1]
if max < resArray[-1]+resArray[0] + resArray[-2]:
    max = resArray[-1]+resArray[0] + resArray[-2]

for i in range(1, n-1):
    if max < resArray[i-1]+resArray[i] + resArray[i+1]:
        max = resArray[i-1]+resArray[i] + resArray[i+1]

print(resArray)
print(f"Output: {max}")
