#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
#и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.
import random

#Пример вывода:
#Сумма 2   комбинация [(1,1)]
#Сумма 3   комбинация [(1,2),(2,1)]
#Сумма 4   комбинация [(1,3),(3,1),(2,2)]
#.......................................
#Выводы комбинаций оформить в список кортежей.

#Вывод произвольных комбинаций
numbers = list(range(1, 7))
print (numbers)
kost1 = random.randrange(1, len(numbers) + 1)
kost2 = random.randrange(1, len(numbers) + 1)
print ("Кость_1:", kost1)
print ("Кость_2:", kost2)
comb = (kost1, kost2)
summ = kost1 + kost2
print("Сумма", summ, "  ", "комбинация [",comb,"]")

#Вывод всех возможных комбинаций
# def function_kosti():
#   kosti = []
#   for i in range(1,7):
#       kost_1 = i + 1
#     for j in range(1,7):
#         kost_2 = j + 1
#       kosti.append((i,j))
#           summ = kost_1 + kost_2
#   return kosti
# print (summ)
# print(function_kosti())





