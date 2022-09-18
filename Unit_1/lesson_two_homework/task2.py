#Преобразуйте переменную age и foo в число 
age = "23"
age = float(age)
print ("age =", age, " - ", type(age))

foo = "23abc"
foo = float(int(bool(foo)))
print ("foo =", foo, " - ", type(foo))

#Преобразуйте переменную age в Boolean
#age = 123abc

#Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)
print ("flag =", flag, " - ", type(flag))

#Преобразуйте значение  в Boolean
str_one = "Privet"
str_two = ""
str_one = bool(str_one)
str_two = bool(str_two)
print ("str_one =", str_one, " - ", type(str_one))
print ("str_two =", str_two, " - ", type(str_two))

#Преобразуйте значение 0 и 1  в Boolean