# Задача № 1
# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек (их число может варьироваться):
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей 
# с одинаковыми индексами после сортировки! “Познакомить” пары нам поможет функция zip, 
# а в цикле распакуем zip-объект и выведем информацию в виде:
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
# Внимание! Если количество людей в списках будет не совпадать, то мы никого знакомить 
# не будем и выведем пользователю предупреждение, что кто-то может остаться без пары!

import sys

def input_people(input_text): # Функция проверки на ошибку при вводе numbers_boys и numbers_girls
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{input_text}'))
            if number >= 0:
              is_OK = True
            else:
              print("Error: Введите число больше нуля или равно нулю.")
        except ValueError:
            print('Error: Вы ввели не число.')
    return number

def input_answer(input_text): # Функция проверки на ошибку при вводе answer
    while True:
        number = input(f'{input_text}')
        if not number.isdigit() or int(number) < 1 or not number.isdigit() or int(number) > 2:
            print("Error: Введите число 1 или 2.")
            continue
        return int(number)

numbers_boys = input_people("Введите количество мужчин в списке: ")
numbers_girls = input_people("Введите количество женщин в списке: ")

while numbers_boys != numbers_girls:
    print("Предупреждение, кто-то может остаться без пары!")
    answer = input_answer("Вы уверены, что хотите продолжить? (1. Да/ 2. Нет) ")
    if answer == 1:
        print("Программа завершается. Знакомить никого не будем.")
        sys.exit()
    else: 
        numbers_boys = input_people("Введите количество мужчин в списке: ")
        numbers_girls = input_people("Введите количество женщин в списке: ")

boys = []
for name in range(numbers_boys):
    name = input("Введите имя партнера: ")
    boys.append(name)

girls = []
for name in range(numbers_girls):
    name = input("Введите имя партнерши: ")
    girls.append(name)

print(boys)
print(girls)
boys.sort()
girls.sort()

zipped_list = list(zip(boys, girls))

print("Идеальные пары: ")
for name in range(len(zipped_list)):
    boys, girls = zip(*zipped_list)
    print(boys[name], " и ", girls[name])


