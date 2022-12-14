# Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.

from random import randrange


def open_letter(template, word, letter):
    for i in range(0, len(word)):               #создаем цикл, в котором для индекса по всей длине массива загаданного слова ищем:
        if word[i] == letter:                   #если в загаданном слове в нужной позиции есть введенная буква то все отлично
            template[i] = letter                #закидываем угаданную букву в шаблон
    return template


words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "Структурная часть сооружения", "Предмет управлеческого воздействия со стороны субъекта"]

i = randrange(len(words))
word = list(words[i])                           #создаем список из слова
template = ["_"]*len(word)                      #создаем шаблон в виде списка с тем же количеством букв
allowed_attempt = 10                            #создаем счетчик неправильных попыток
print(desc_[i])

while "_" in template:                          #создаем цикл игры
    print(template)                             #смотрим как выглядит шаблон, есть ли в нем буквы
    letter = str(input("Введите букву: "))      #вводим букву
    if letter not in word:                      #если буквы в слове нет, то ошибка
        allowed_attempt -= 1
        print(f"Нет буквы. Осталось {allowed_attempt} неудачных попыток")
    else:
        print(f"Есть! Откройте {letter}")
        template = open_letter(template, word, letter)
    if allowed_attempt == 0:                    #если ошибок много, то проигрыш
        break
if "_" not in template:
    print("вы выиграли")                        #если все буквы разгаданы, то выигрыш
else:
    print("Вы проиграли")