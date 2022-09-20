#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

A = float(input("Введите точку А: "))
B = float(input("Введите точку B: "))
C = float(input("Введите точку C: "))
if (A < 0 and C < 0 and abs(A)>abs(C)) or (A > 0 and C > 0 and abs(A)>abs(C)):
    AC = abs(A) - abs(C)
else:
    AC = abs(A) + abs(C)

#summ = AC + BC
print("длина отрезка AC =", AC)
#print("длина отрезка BC =", BC)
#print("сумма =", summ)
