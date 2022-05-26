# Примеры LIST comprehension

nums = [n for n in range(1, 6)]  # Выводит числа от одного до 5

squares = [n * n for n in nums]  # Возводит число из списка переменной (nums) в степень своего же значения

odd_squares = [n*n for n in nums if n%2 == 1] # Возводит число из списка переменной (nums) в степень своего же значения
# и выводим только нечетные числа

matrix = [[x for x in range(1, 4)] for y in range(1, 4)]  # Создает список в списке (2-х мерный массив).
# Выход: [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

even_squares = [n for n in nums if n%2 == 0] # Выводит четные значения из списка переменной (nums)


# Примеры DICT comprehension

# Пример
MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',

}

a = {num: num**2 for num in range(1, 11)} # Создаем словарь в котором значение ключа будет ключь в квадрате

b = {key.upper(): value for key, value in MLB_team.items()} # Возводит все буквы имени ключа в верхний регистр

c = {key: value + ': Name Team' for key, value in MLB_team.items()} # Добовляем к нашему значению строку

d = {key: value.replace(value, 'Loose') for key, value in MLB_team.items() if key == "Boston"} #  Меняем наше значение ключа,
# если  условие в циклe выполнится

e = {key: value for key, value in ((1, "one"), (2, 'two'), (3, 'three'))} # Создаем наш словарь из пар-елементов вложенного
# картежа


# Примеры SET comprehension

# Пример множества
number = [10, '3', 3, 10, '56']

unique_number_1 = {int(element) for element in number }  # Записываем в наше множество елементы из списка
# переменной (number)

unique_string = {element for element in number if isinstance(element, str)}  # Записываем в наше множество строковые
# литералы из списка переменной (number)

unique_number_2 = {element ** 2 for element in number if isinstance(element, int)}  # Возводим числовой литерал
# переменной (number) в квадрат

unique_number_3 = {element for element in range(11)}  # Записываем в сет числа от 0-10

even_number_4 = {element for element in range(11) if element % 2 == 0}  # Записываем во множество четные числа от 0-10
