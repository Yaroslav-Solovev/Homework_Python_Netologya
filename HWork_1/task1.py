# Задача № 1. Квадрат и прямоугольник.
def InputNumbers1(inputText): # Функция проверки на ошибку при вводе
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f'{inputText}'))
            if number > 0:
              is_OK = True
            else:
              print('Введите число больше 0.')
        except ValueError:
            print('Error: Вы ввели не число.')
    return number
  
a = InputNumbers1('Введите длину стороны квадрата: ') # 3
p1 = a * 4
s1 = a ** 2
print('Вывод: ')
print('Периметр: ', p1) # 12
print('Площадь: ', s1) # 9

b1 = InputNumbers1('Введите длину стороны прямоугольника: ') # 3
b2 = InputNumbers1('Введите ширину стороны прямоугольника: ') # 4
p2 = (b1 + b2) * 2
s2 = b1 * b2
print('Вывод: ')
print('Периметр: ', p2) # 14
print('Площадь: ', s2) # 12

# Задача № 3. Разделитель.
def task3():
  global p1
  global s2
  sum = int(round(p1)) + int(round(s2)) # сумма периметра квадрата и площади прямоугольника
  n = str(input('Введите симбол: '))
  print(*[n for _ in range (len(n), sum + 1)], sep='')
task3()
