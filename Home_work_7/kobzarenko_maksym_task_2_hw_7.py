# Функуия которая ничего не возвращает
def greetings():
    print('Hello, my dear User!')


# Пустая функуия с заглушкой (pass)
def number_squared():
    pass


# Пустая функуия с заглушкой (...)
def number_cubed():
    ...


#  Функция возводит аргумент функции в квадрат
def number_squared(number):
    return number ** 2


# Сравнивает аргументы функции и показывает какое число больше или меньше, аргументы равны воводит "равно"
def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')


# Функция приведствует пользователя
def greetings(name, surname):
    print(f'Hello, my dear {name} {surname}')


# Возвращает сумму 2-х арягументов
def summa_two(x, y):
    return x + y


#  Функция с ключевыми параметрами
def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)
