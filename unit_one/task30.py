#todo: Найти сумму элементов матрицы
# Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

#Вариант 1
matrix = [[1, 2, 3], [4, 5, 6]]
def msum(matrix):
    summ_of_elements = sum([sum(i) for i in matrix])
    print("Сумма элементов =", summ_of_elements)

msum(matrix)

#Вариант 2
def msum(matrix):
    summ_of_elements = sum([col for row in matrix for col in row])
    print("Сумма элементов =", summ_of_elements)

msum(matrix)

