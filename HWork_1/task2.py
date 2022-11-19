# Задача № 2. Приложение для финансового планирования.
def InputNumbers2(inputText): # Функция проверки на ошибку при вводе
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f'{inputText}'))
            if number >= 0:
                is_OK = True
            else:
                print('Введите число больше или равно 0.')
        except ValueError:
            print('Error: Вы ввели не число.')
    return number
zarplata = InputNumbers2('Введите заработную плату в месяц: ') # 100000
ipoteka = InputNumbers2('Введите, какой процент(%) уходит на ипотеку: ') / 100 # 30
live = InputNumbers2('Введите, какой процент(%) уходит на жизнь: ') / 100 # 50

print('Вывод: ')
print('На ипотеку было потрачено за год: ', zarplata * ipoteka * 12, ' рублей.') # 360000
print('Было накоплено за год: ', (zarplata - (zarplata * ipoteka) - (zarplata * live)) * 12, ' рублей.') # 240000