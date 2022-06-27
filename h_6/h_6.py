# Task 34:
# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

# def polynom(pol, res):
#     pol1 = pol.split("+")
#     for i in pol1:
#         pol2 = i.strip().split('*') 
#         if(len(pol2)>1):
#             if(pol2[1] in res.keys()):
#                 res[pol2[1]]=res[pol2[1]]+int(pol2[0])
#             else:
#                 res[pol2[1]]=int(pol2[0])
#         else: 
#             if(0 in res.keys()):
#                 res[0]=res[0]+int(pol2[0]) 
#             else:
#                 res[0]=int(pol2[0])

# f1 = open("polynom1.txt", "r") 
# p1 = f1.read() 
# f1.close()

# f2 = open("polynom2.txt", "r") 
# p2 = f2.read() 
# f2.close()

# result = {}

# polynom(p1, result)
# polynom(p2, result)
  
# res = ""
# for i in result:
#     if(res!=""):
#         res += " + "
#     res += str(result[i])
#     if(i!=0):
#         res += ' *' + i

# res_f = open("polynom3.txt", "w") 
# res_f.write(res)
# res_f.close()
# print(res)

# Task 39:
# Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека

# candies = int(input("Введите количество конфет: "))
# player = 1
# max_can = int(input("Введите максимальное количество конфет за ход: "))
# while candies !=0:
#         user = int(input(f"Игрок {player}: введите количество от 1 до {max_can}(но не больше остатка): "))
#         if user > max_can or user < 1 or user > candies:
#             print("Вы ввели некорректное значение, повторите ввод: ")
#             continue    
#         candies = candies - user
#         print(f"Остаток: {candies}")
#         if player == 1:
#             player = 2
#         else:
#             player = 1
# print(f"Выиграл {player} игрок")       

