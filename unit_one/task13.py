#done: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

#Вар1
N = 0
list = [1, 278, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for N in list:
    list[i] = N + 1
    i = i + 1
print(list)

#Вар2
N = 0
list = [1, 278, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for N in list:
    list.remove(N)
    N = N + 1
    list.insert(i, N)
    i = i + 1
print(list)
