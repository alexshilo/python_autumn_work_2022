#done: Даны переменные A, B, C. Написать код, который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
A = 3
B = 1
C = 2
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10

if (A <= B and A <= C):
    if B <= C:
        A, B, C = A, B, C
        print("A=", A)
        print("B=", B)
        print("C=", C)
    elif B > C:
        A, B, C = A, C, B
        print("A=", A)
        print("B=", B)
        print("C=", C)
if (B <= A and B <= C):
    if A <= C:
        A, B, C = B, A, C
        print("A=", A)
        print("B=", B)
        print("C=", C)
    elif A > C:
        A, B, C = B, C, A
        print("A=", A)
        print("B=", B)
        print("C=", C)
if (C <= B and C <= A):
    if B <= A:
        A, B, C = C, B, A
        print("A=", A)
        print("B=", B)
        print("C=", C)
    elif B > A:
        A, B, C = C, A, B
        print("A=", A)
        print("B=", B)
        print("C=", C)