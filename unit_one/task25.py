#todo: Убрать повторяющиеся буквы и лишние символы
# Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
# Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

# Input             	            Output
#
# apple	                        aple
# 25.04.2022 Good morning !!	    godmrni

x = "apple"
y = "25.04.2022 Good morning !!"

output_x = "".join(dict.fromkeys(x))
output_y = "".join(dict.fromkeys(filter(str.isalpha, y.lower())))

print (output_x)
print (output_y)