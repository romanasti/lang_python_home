# Task 33:
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# a = int(input("Задайте натуральную степень k: "))
# f = open('polynom.txt', 'w')
# for i in range(a):
#     b = random.randint(0,100)
#     f.write(f"{b} * x^{a-i} + ")
# f.write("5 = 0")
# f.close()

# Task 35:
# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# with open('spisok.txt', 'r') as f:
#     lines = " ".join(f.readlines())
# lines = lines.replace(" ", "")
# a = [int(x) for x in lines]
# for i in range(1,len(a)):
#     if a[i-1] != a[i] - 1: print(f"Недостающий элемент -->", a[i-1]+1)

# Task 43:
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# num = [1, 2, 3, 5, 1, 5, 3, 10]
# new = []
# for i in range(len(num)):
#     for j in range(len(num)):
#         if i != j and num[i] == num[j]:
#             break
#     else: new.append(num[i])
# print(f"Уникальные элементы -->", new)
