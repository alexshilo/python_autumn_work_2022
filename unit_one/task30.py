#todo: Найти сумму элементов матрицы
# Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

matrix = [[1, 2, 3], [4, 5, 6]]
def msum(matrix):
    summ_of_elements = sum([sum(i) for i in matrix])
    print("Сумма элементов =", summ_of_elements)

msum(matrix)