from pprint import pprint

def input_numbers_person_count(input_text):
    while True:
        number = input(f'{input_text}')
        if not number.isdigit() or int(number) < 1:
            print("Error: Введите число больше нуля.")
            continue
        return int(number)

def cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            products = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                products.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = products
    return cook_book

cook_book = cook_book()

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = dict()
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredients_dish in cook_book[dish_name]:
                meas_list = dict()
                if ingredients_dish['ingredient_name'] not in ingredients_list:
                    meas_list['measure'] = ingredients_dish['measure']
                    meas_list['quantity'] = ingredients_dish['quantity'] * person_count
                    ingredients_list[ingredients_dish['ingredient_name']] = meas_list
                else:
                    ingredients_list[ingredients_dish['ingredient_name']]['quantity'] = ingredients_list[ingredients_dish['ingredient_name']]['quantity'] + ingredients_dish['quantity'] * person_count
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingredients_list

print('############# Задача № 1 ###############')
pprint(cook_book)
print('############# Задача № 2 ###############')
pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count = input_numbers_person_count('Введите количество персон: ')))
