# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
# Подготовил два варианта решения

while True:
    try:
        n = int(input("Введите длину шоколадки: "))
        m = int(input("Введите ширину шоколадки: "))
        k = int(input("Введите количество кусочков: "))
        if k < m * n:
            if (k % m == 0 or k % n == 0):
                print(f'Можно ломать!')
                break
        elif k == m * n:
            print('Ломать не нужно! Забирайте целиком!')
            break
        else:
            print('Столько кусочков нет!')
            break
    except:
        print('Некорректный ввод. Попробуйте еще раз!')
