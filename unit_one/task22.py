# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
#  В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

myfile = open("message.txt", "r", encoding="utf-8")

cyr_low = set("съешь же еще этих мягких французских булок да выпей чаю".replace(" ", ""))
cyr_high = [x.upper() for x in cyr_low]
sorted_cyr_low, sorted_cyr_high = sorted(cyr_low), sorted(cyr_high)
sorted_cyr = sorted_cyr_low + sorted_cyr_high
print(sorted_cyr)

shift = 0
count = len(myfile.readlines())
myfile.seek(0,0)
encryption = ''
while shift <= count:
    shift += 1
    line = myfile.readlines()
    for i in line:
        if i.isupper():

            ######## в работе"
            # i_unicode = ord(i)
            # i_index = ord(i) - ord("А")
            # new_index = (i_index + shift)%32
            # new_unicode = new_index + ord("А")
            # new_character = chr(new_unicode)
            # encryption = encryption + new_character
        else:
            encryption += i

print(encryption)










