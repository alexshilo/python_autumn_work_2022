#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

x1 = "8 5 12 12 15"
x1_list = x1.split(" ")
x1_numbers = [int(num) for num in x1_list]
print(''.join([chr(number + 96) for number in x1_numbers]))

x2 = "8 5 12 12 15 , 0 23 15 18 12 4 !"
x2_list = x2.split(" ")
print(x2_list)


input_1 = "8 5 12 12 15"
input_2 = "8 5 12 12 15 , 0 23 15 18 12 4 !"
#заменяем цифры на буквы алфавита
import string
words_list = list(string.ascii_lowercase) #создаем строку с алфавитом и делаем список
input1_list = list(input_1) #создаем листы из input_1 и input_2
input2_list = list(input_2)
print(words_list,"\n", input1_list,"\n", input2_list)

#делаем замену цифр на буквы
for i in input_1:
    if symbol == int:

#убираем лишние пробелы

