# Примеры функции "all". Если хоть одно условие или элемент итерируемого объекта равен истене то функция "all" возвращает
# 'True'. Если все условия или элементы итерируемого объекта не являються истиной то функция "all" вернёт "False"

print(all((2 > 1, 'k' in 'kotiki')))  # Выведит 'True'

print(all((2 < 1, 'k' in 'dog')))  # Выведит "False"

# Пример функции "any". Если все условия или элементы итерируемого объекта равны истене то функция "any"
# возвращеает "True". Если хоть одно условие не соответсвует истине функция "any" возвращает "False"

print(any((2 > 1, 'k' in 'dog')))  # Выведит 'True'

print(any((2 > 34, [], False)))  # Выведит "False"

# Пример функции "filter". Функция "filter" выводит все элемнеты итерируемого объекта которые выполняют истину для нашей
# вложенной функции в функции "filter". *****Примечание вложенная функция должна выводить булиновское значение.
# Функция "filter" выводит сылку на объект функции.
list_my = [32, [1, 2, 3, 4], False, (), '3' in '34', "abra cadabra", [2.23, 3, 5, False]]  # Пример

print(list(filter(lambda element: isinstance(element, list), list_my)))

# Пример функции "map". Функция "map" применят вложеную функцию ко всем элементам итерируемого объекта. И выводит сылку
# на объет функции

list_my_1 = [2.0125, 4.5585, 846.532222, 46.00005]  # Пример

round_list_my_1 = list(map(int, list_my_1))  # Преобразовыаем елементы нашего списка "list_my_1" в целые числа и вывоим
# их в виде списка

print(round_list_my_1)

# Премир декораторов

ukrainian_namber: dict = {"Oleg": "0932566478", 'Roman': '0986541298', 'Oksana': '+380965481237'}  # Пример


#  Этот декоратор выводит список украинских операторов и их код на который они начинаються
def decorator_operators_ukrainian_number(func):
    def wrapper(*args, **kwargs):
        print("Оператор Life - +38 (093), (063)", "Оператор Kievstar - +38 (097), (096) ", sep='\n')
        numbers = func(*args, **kwargs)
        return numbers

    return wrapper


@decorator_operators_ukrainian_number
# Это функция дописывает мобильный код Украины(+38) к номеру телефона если в нем не указан код страны. За аргумент берет
# словарь
def cod_ukrainian_number(dictionary):
    for name, number in dictionary.items():
        if '+38' not in number:
            dictionary[name] = '+38' + number
        else:
            dictionary[name] = number
    return dictionary


print(cod_ukrainian_number(ukrainian_namber))
