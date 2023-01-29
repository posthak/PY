# Уровень 1: # 1 действие  # 2 аргумента 12 + 15
# Уровень 2: # Количество действий произвольное # 12 + 15 - 4
# Уровень 3: # Действия имеют приоритет # 12 - 4*2 +6/3
# Уровень 4  * (Дополнительная задача, сдавать не обязательно) # Действия разделяются скобками # (12 - 4) * 2

import os
def clear(): return os.system('clear')


def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b


n = '22 * 300 - 14 + 10 * 10 * 10'
# n = '12 + 15'
# n = '12 + 15 - 4'
m = n.split()
numb = []
chars = []

dictionary = \
    {"+": 1,
     "-": 1,
     "*": 2,
     "/": 2}


def HighElement(list):
    if list:
        return list[len(list)-1]


def GetPrio(s):
    for i in dictionary:
        if i == s:
            return dictionary[i]
    return 0


clear()
i = 0
while i < len(m):
    if GetPrio(m[i]) < 1:
        numb.append(m[i])

        if i+1 == len(m):
            for z in range(0, len(chars)):
                x = int(numb.pop())
                y = int(numb.pop())
                numb.append(calc(y, x, HighElement(chars)))
                chars.pop()
        i = i+1
    else:
        if len(chars) > 0:
            if GetPrio(m[i]) <= GetPrio(HighElement(chars)):
                x = int(numb.pop())
                y = int(numb.pop())
                numb.append(calc(y, x, HighElement(chars)))
                chars.pop()
            else:
                chars.append(m[i])
                i = i+1
        else:
            chars.append(m[i])
            i = i+1
print('Результат выражения: {}  =  {}'.format(n, numb[0]))
