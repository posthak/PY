def ReadDataFromFile(name):
    with open(name, 'r', encoding='utf8') as datafile:
        return list(map(lambda result: result.strip('\n').split(','), datafile))


def SaveDataToFile(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list + '\n')


def CollectRoutes(busData, driverData, routeData):
    fields = '|Номер   |Гос номер|Имя      |\n|маршрута|автобуса |Водителя |'
    print(f'{"-"*30}\n{fields}\n{"-"*30}')
    [print('|{:>8}|{:>9}|{:>9}|'.format(routeNum, GetField(busId, busData),
                                        GetField(driverId, driverData)))for routeId, routeNum, busId, driverId in routeData]
    print("-"*30)
    input("Для продолжения нажмите Enter>")


def PrepareAndPrint(col):
    fields = '|Id      |Name      |'
    print(f'{"-"*21}\n{fields}\n{"-"*21}')
    [print('|{:>8}|{:>10}|'.format(id, name))for id, name in col]
    print("-"*21)
    input("Для продолжения нажмите Enter>")


def GetField(id, col):
    z = [y for x, y in col if id.strip() == x.strip()]
    return z[0] if z else 'N/A'


def print_bus():
    return PrepareAndPrint(ReadDataFromFile('bus.txt'))


def add_bus():
    SaveDataToFile('bus.txt', input("Введите параметры автобуса: "))
    print("Автобус добавлен!")


def print_driver():
    return PrepareAndPrint(ReadDataFromFile('driver.txt'))


def add_driver():
    SaveDataToFile('driver.txt', input("Введите водителя: "))
    print("Водитель добавлен!")


def print_route():
    CollectRoutes(ReadDataFromFile('bus.txt'), ReadDataFromFile('driver.txt'),
                  ReadDataFromFile('route.txt'))


def add_route():
    SaveDataToFile('route.txt', input("Введите маршрут: "))
    print("Маршрут добавлен!")
