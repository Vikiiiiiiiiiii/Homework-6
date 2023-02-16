# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Пример:
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
lst = int(input("Введите размер списка: "))
mas=[randint(-20, 30) for i in range(lst)]
print(mas)

max=int(input("MAX= "))
min=int(input("MIN= "))

lst_1 =[]
if max>=min:
    for i in range(len(mas)):
        if max>=mas[i] and min<=mas[i]:
            lst_1.append(i)

    print("Кол-во:",len(lst_1))
    print("Индексы:", lst_1)