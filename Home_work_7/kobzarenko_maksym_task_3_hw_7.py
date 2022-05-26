# Написать функцию которая в качестве аргумента принимает размер стороны квадрата, а возвращает кортеж в котором лежат три значения:

# периметр квадрата
# диагональ квадрата
# площадь квадрата

# Импортируем из матемтческого модуля функцию квадратного корня
from math import sqrt


# Создаём функцию которая в качестве аргумента принимает размер стороны квадрата
def square(side_length):
    perimeter_square = side_length * 4  # Считаем периметр квадрата
    square_area = side_length ** 2  # Считаем площадь квадрата
    diagonal_square = round(side_length * sqrt(2), 2)  # Считаем диагональ квадрата
    # Выводим наши значения (периметр, квадрат, площадь) в виде картежа
    return print(tuple([
        f'perimeter square = {perimeter_square}, diagonal square = {square_area}, diagonal square = {diagonal_square}']))


print(square(5))
