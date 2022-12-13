# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Input 3 digits number: ')
a = int(input())
if len(str(a)) == 3:
    res = a % 10 + int(a/10) % 10 + int(a/100) % 10
    print(f"{a} -> {res} ({int(a/100)%10} + {int(a/10)%10} + {a%10})")
else:
    print('You have entered wrong number')
