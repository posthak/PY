# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12

text = str(input("Input some text on RUS or ENG languages: "))
dictionary = \
    {1: 'AEIOULNSTRАВЕИНОРСТ',
     2: 'DGДКЛМПУ',
     3: 'BCMPБГЁЬЯ',
     4: 'FHVWYЙЫ',
     5: 'KЖЗХЦЧ',
     8: 'JXШЭЮ',
     10: 'QZФЩЪ'}

amount = 0
for s in text:
    for k in dictionary:
        if dictionary[k].find(s.upper()) >= 0:
            amount += k

print("\n")
print(f"Input: {text}")
print(f"Output: {amount}")
