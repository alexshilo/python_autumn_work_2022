#done: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

A = float(input("Введите точку А: "))
B = float(input("Введите точку B: "))
C = float(input("Введите точку C: "))

AC = abs(A - C)
BC = abs(B - C)
summ = AC + BC

print("длина отрезка AC =", AC)
print("длина отрезка BC =", BC)
print("сумма =", summ)

