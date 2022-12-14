# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
# Подготовил два варианта решения

# I Решение, где можно отломить точное количество долек в ряде
width = int(input('Input  width of chocolate: '))
height = int(input('Input height of chocolate: '))
piece = int(input('Input number of pieces to take: '))

if (piece == width or piece == height) and not (width < 2 or height < 2):
    print(f"{piece} {width} {height} -> yes")
else:
    print(f"{piece} {width} {height} -> no")

# II Решение, где можно отломить заданое кол-во долек если даже в ряде их больше
width = int(input('Input  width of chocolate: '))
height = int(input('Input height of chocolate: '))
piece = int(input('Input number of pieces to take: '))

if (piece <= width or piece <= height) and not (width < 2 or height < 2):
    print(f"{piece} {width} {height} -> yes")
else:
    print(f"{piece} {width} {height} -> no")
