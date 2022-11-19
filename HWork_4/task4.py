# Задание 4

# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т.е. в данном примере скрипт должен возвращать ‘yandex’.

stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_chanel = ''
for chanel in stats.keys():
    if stats[chanel] > stats.get(max_chanel,0):
        max_chanel = chanel
print('Канал с максимальным объемом: ', max_chanel)