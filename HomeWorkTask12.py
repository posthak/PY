# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

def GetXY(s, p):
    for x in range(1, 1000):
        y = s-x
        if (x <= y and x*y == p):
            print(f"{s,p} -> {x, y}")
            break
        elif x > y or x > 500:
            print("You captured incorrect numbers, run one more")
            break


sNumber = int(input("Input total sum of numbers S: "))
pNumber = int(input("Input total multiple of numbers P: "))
GetXY(sNumber, pNumber)
