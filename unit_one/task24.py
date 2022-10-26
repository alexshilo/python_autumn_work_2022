#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

x1 = "8 5 12 12 15"
x1_list = x1.split(" ")
x1_numbers = [int(num) for num in x1_list]
print(''.join([chr(number + 96) for number in x1_numbers]))



