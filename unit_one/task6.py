#done: Дана сторона квадрата a. Найти его площадь S = a²
# Примечание: сторону квадрата получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

a = float(input("Введите длину стороны квадрата а: "))
if a > 0:
    print ("Площадь квадрата S =", a ** 2)
else:
    print ("Нет решения")