# Задача №1
# Ипотечный калькулятор В новом банке решили начать выдавать ипотеку. Появилась необходимость разработать для них ипотечный калькулятор. 
# Нужно рассчитать финальную процентную ставку по ипотеке. От каких критериев зависит скидка на ипотеку:
#1.Если клиент из Дальнего Востока (список субъектов, входящих в регион, определить самостоятельно), то базовая ставка становится 2%.
#2.Если количество детей больше 3, то базовая ставка уменьшается на 1%.
#3.Если у клиента зарплатный проект в этом банке, то базовая ставка уменьшается на 0.5%.
#4.Если в этом же банке будет оформлена страхование, то базовая ставка уменьшается на 1.5% 
#Базовую процентную ставку выбрать самостоятельно. Если клиент оформляет ипотеку по дальневосточной программе, то остальные скидки не применяются.
#P.s. При использовании функции по примеру input_numbers3 для base_rate, при вводе числа типа float "2.4 и т.п." 
# выводится ошибка AttributeError: 'float' object has no attribute 'isdigit' поэтому ипользовал стандартный try-except

def input_numbers1(input_text): # Функция проверки на ошибку при вводе base_rate
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f'{input_text}'))
            if number > 0:
              is_OK = True
            else:
              print("Error: Введите число больше нуля.")
        except ValueError:
            print('Error: Вы ввели не число.')
    return number

def input_numbers2(input_text): # Функция проверки на ошибку при вводе salary_project и create_insurance
    while True:
        number = input(f'{input_text}')
        if not number.isdigit() or int(number) < 1 or not number.isdigit() or int(number) > 2:
            print("Error: Введите число 1 или 2.")
            continue
        return int(number)

def input_numbers3(input_text): # Функция проверки на ошибку при вводе number_child
    while True:
        number = input(f'{input_text}')
        if not number.isdigit() or int(number) < 0:
            print("Error: Введите число больше или равно нулю.")
            continue
        return int(number)

def input_numbers4(input_text): # Функция проверки на ошибку при вводе live_client
    while True:
        number = input(f'{input_text}')
        if not number.isdigit() or int(number) < 0 or not number.isdigit() or int(number) >= len(list_subject_rf):
            print("Error: Введите число из списка.")
            continue
        return int(number)

list_subject_rf = [
    "Такого региона нет в списке", "Республика Бурятия", "Республика Саха (Якутия)", "Забайкальский край", 
    "Камчатский край", "Приморский край", "Хабаровский край", "Амурская область", 
    "Магаданская область", "Сахалинская область", "Еврейская автономная область", 
    "Чукотский автономный округ"
    ]
numer_subject_rf = enumerate(list_subject_rf)

base_rate = input_numbers1("Введите базовую процентную ставку на ипотеку: ")
if base_rate > 1: base_rate = round(base_rate/100, 3)
print()
print(list(numer_subject_rf))
print()
live_client = input_numbers4("Выберите регион Вашего местожительства из списка, введя его порядковый номер (если таковой имеется): ")
for i in range(len(list_subject_rf)):
    if live_client != 0 and live_client == i:
        base_rate = 0.02

if base_rate == 0.02:
    print('Финальная процентная ставка по ипотеке: ', base_rate)
else:
    number_child = input_numbers3("Введите количество детей: ")
    salary_project = input_numbers2("Зарплатный проект находится в нашем банке (1. Да/ 2. Нет)?: ")
    create_insurance = input_numbers2("Вы желаете оформить страхование (1. Да/ 2. Нет)?: ")
    if number_child >= 3:
        base_rate = base_rate - 0.01
    if (salary_project == 1):
        base_rate = base_rate - 0.005
    if (create_insurance == 1):
        base_rate = base_rate - 0.015
    if base_rate < 0.02:
        print('Финальная процентная ставка по ипотеке c учетом скидок: ', 0.02)
    else: print('Финальная процентная ставка по ипотеке: ', round(base_rate, 3))