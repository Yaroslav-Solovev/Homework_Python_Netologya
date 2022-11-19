# Задание №2
# Разработать приложение для определения знака зодиака по дате рождения.
# Введите месяц: март
# Введите число: 6
# Вывод:
# Рыбы

def input_numbers(input_text): # Функция проверки на ошибку при вводе my_date
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{input_text}'))
            if arr_days[0] <= number <= arr_days[30]:
              is_OK = True
            else:
              print("Error: Вы ввели не число месяца.")
        except ValueError:
            print('Error: Вы ввели не число.')
    return number

arr_month = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
arr_zodiak = ["овен", "телец", "близнецы", "рак", "лев", "дева", "весы", "скорпион", "стрелец", "козерог", "водолей", "рыбы"]

arr_days = []
for i in range(1,32):
    arr_days.append(i)

my_month = input("Введите название месяца Вашего рождения: ")
my_month = my_month.lower()
my_month = [my_month]
my_date = input_numbers("Введите день Вашего рождения: ")

if my_month[0] == arr_month[2]: 
    if my_date >= 21:
        print("Ваш знак зодиака: ", arr_zodiak[0])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[11])
elif my_month[0] == arr_month[3]: 
    if my_date >= 20:
        print("Ваш знак зодиака: ", arr_zodiak[1])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[0])
elif my_month[0] == arr_month[4]: 
    if my_date >= 21:
        print("Ваш знак зодиака: ", arr_zodiak[2])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[1])
elif my_month[0] == arr_month[5]: 
    if my_date >= 21:
        print("Ваш знак зодиака: ", arr_zodiak[3])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[2])
elif my_month[0] == arr_month[6]: 
    if my_date >= 23:
        print("Ваш знак зодиака: ", arr_zodiak[4])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[3])
elif my_month[0] == arr_month[7]: 
    if my_date >= 23:
        print("Ваш знак зодиака: ", arr_zodiak[5])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[4])
elif my_month[0] == arr_month[8]: 
    if my_date >= 23:
        print("Ваш знак зодиака: ", arr_zodiak[6])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[5])
elif my_month[0] == arr_month[9]: 
    if my_date >= 23:
        print("Ваш знак зодиака: ", arr_zodiak[7])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[6])
elif my_month[0] == arr_month[10]: 
    if my_date >= 22:
        print("Ваш знак зодиака: ", arr_zodiak[8])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[7])
elif my_month[0] == arr_month[11]: 
    if my_date >= 22:
        print("Ваш знак зодиака: ", arr_zodiak[9])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[8])
elif my_month[0] == arr_month[0]: 
    if my_date >= 20:
        print("Ваш знак зодиака: ", arr_zodiak[10])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[9])
elif my_month[0] == arr_month[1]: 
    if my_date >= 19:
        print("Ваш знак зодиака: ", arr_zodiak[11])
    else:
        print("Ваш знак зодиака: ", arr_zodiak[10])
