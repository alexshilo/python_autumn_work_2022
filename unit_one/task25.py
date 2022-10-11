#todo: Убрать повторяющиеся буквы и лишние символы
# Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
# Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

# Input             	            Output
#
# apple	                        aple
# 25.04.2022 Good morning !!	    godmrni

input_1 = "apple"
input_2 = "25.04.2022 Good morning !!"
print("".join(dict.fromkeys(input_1)))
print("".join(dict.fromkeys(filter(str.isalpha, input_2.lower()))))

