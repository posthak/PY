# Домашнее задание Семинар 6
# import json
import os


def DeleteContact(fileName, text):
    with open(fileName, "r", encoding="utf8") as f:
        data = list(map(lambda index: index, f))
        data = list(filter(lambda x: not x.find(text) >= 0, data))
    with open(fileName, "w", encoding="utf8") as file:
        list(map(lambda x: file.write(x), data))
    if not data:
        print('Contact was not deleted!')
    else:
        print('Contact was deleted!')


def PrintFile(data):
    list(map(lambda x: print(x, end=""), data))


def FindByName(file_name, text):
    with open(file_name, "r", encoding="utf8") as file:
        data = file.readlines()
        data = list(filter(lambda x: x.find(text) >= 0, data))
        data = list(map(lambda x: print(x), data))


def ChangeNum(file_name, oldNum, newNum):
    with open(file_name, "r", encoding="utf8") as file:
        data = file.readlines()
        data = list(map(lambda x: x.replace(oldNum, newNum), data))
    with open(file_name, "w", encoding="utf8") as file:
        list(map(lambda x: file.write(x), data))
    print('Contact was changed!')


def ReadFile(name):
    with open(name, "r", encoding="utf8") as file:
        list(map(lambda x: print(x, end=""), file.read()))


def AddLineFile(fileName, text):
    with open(fileName, "a", encoding="utf8") as file:
        file.write(text+"\n")
    print('Contact was added!')


def clear(): return os.system('clear')


fName = 'file.txt'
clear()
while True:
    menuitems = \
        ('1 - Показать все записи',
            '2 - Найти запись по вхождению частей имени',
            '3 - Найти запись по телефону',
            '4 - Добавить новый контакт',
            '5 - Удалить контакт',
            '6 - Изменить номер телефона у контакта',
            '7 - Выход')

    print('Введите номер действия:')
    list(map(lambda x: print(x), menuitems))
    menu = int(input())
    clear()
    if menu == 1:
        ReadFile(fName)
    elif menu == 2:
        text = input("Input name: ")
        FindByName(fName, text)
    elif menu == 3:
        text = input("Input number: ")
        FindByName(fName, text)
    elif menu == 4:
        text = str(input("Input new contact:"))
        AddLineFile(fName, text)
    elif menu == 5:
        text = str(input("Input name or mob. num: "))
        DeleteContact(fName, text)
    elif menu == 6:
        oldNum = input("Input number to change: ")
        newNum = input("Input new number to replace: ")
        ChangeNum(fName, oldNum, newNum)
    elif menu == 7:
        quit()
