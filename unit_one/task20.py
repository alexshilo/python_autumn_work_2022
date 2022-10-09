#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# Содержимое файла import_this.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# выходные данные
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

f = open("import_this.txt", "wt")
lines = ["Beautiful is better than ugly.\n", "Explicit is better than implicit.\n", "Simple is better than complex.\n", "Complex is better than complicated.\n"]
f.writelines(lines)
f = open("import_this.txt", "rt")
output_data = f.readlines()
output_data.reverse()
print ("".join(output_data))

