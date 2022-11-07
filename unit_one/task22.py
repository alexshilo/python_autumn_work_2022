# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
#  В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

myfile = open("message.txt", mode = "r", encoding = "utf-8")

cyr_low = set("съешь же еще этих мягких французских булок да выпей чаю".replace(" ", ""))
cyr_high = [x.upper() for x in cyr_low]
sorted_cyr_low, sorted_cyr_high = ''.join(sorted(cyr_low)), ''.join(sorted(cyr_high))
print(sorted_cyr_low)
print(sorted_cyr_high)


count = len(myfile.readlines())
myfile.seek(0,0)
encryption = ''
shift = 0

while shift <= count:                          #поправить содержимое цикла
    shift += 1
    line = myfile.readlines()
    for letter in line:
        x = letter.lower()
        position = sorted_cyr_low.find(x)
        new_position = position - shift
        if letter in sorted_cyr_low:
            encryption = encryption + sorted_cyr_low[new_position]
        elif letter in sorted_cyr_high:
            encryption = encryption + sorted_cyr_high[new_position]
        else:
            encryption = encryption + letter

print(encryption)










