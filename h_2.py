# Task 1:
# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр(отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11

# number = (input("Введите положительное число: "))
# sum = 0
# for i in number:
#     if i!= ".":
#         sum += int(i)
# print(f"Сумма чисел -->",sum)

# Task 2:
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

# num = int(input("Введите число: "))
# factorial = 1
# for i in range(1,num+1):
#     factorial *= i
# print(f"Факториал числа {num} равен =",factorial)

# Task 3:
# Реализуйте случайное перемешивания списка.
# Пример:
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True ']
# Результат -> [250, 3.14, 'True ', 'Веселый пианист']

# import random
# list = ['Веселый пианист', 250, 3.14, 'True ']
# print("Исходный вариант -->",list)
# random.shuffle(list)
# print("Результат -->",list)



