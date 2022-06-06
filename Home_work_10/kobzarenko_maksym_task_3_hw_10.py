# Импортируем из модуля "functools" метод "wraps"
from functools import wraps


# Создаем дэкоратор который принимает какой-то текст и в котором будет выводиться колличество методов объекта
def decoratore(some_text: str):  # Функция принимает какой-то текст. ДОПОЛНИТЕЛЬНЫЙ АРГУМЕНТ декоратора
    def decore_amound_method(func):  # Функция которая в аргументе принимает другую функцию
        @wraps(func)  # С помощью этого декоратора мы сохраняем имя вложеной в аргумент функции
        def wrapper(object):
            mount_method: int = len(func(object))  # Считаем колличество методов для данного объкта. Список методов
            # берем из того что возвращает вложенная функции в аргументе
            print(func(object), f'{some_text} {mount_method}', sep='\n')

        return wrapper

    return decore_amound_method


@decoratore("Need to learn")
# Создаем функцию которя будет выводить только методы объекта, которого мы укажем в аргументе функции
def show_method(object):
    all_method_object: list = dir(object)  # Выводим обычные и магические методы объекта.
    only_method_object: list = []  # Записываем только обычные методы объекта

    for method in all_method_object:  # Проходим по всем объектам списка "all_method_object"
        # Если в названии метода нету нижнего подчеркивания "_", то мы его добовляем в наш список "only_method_object".
        if '_' not in method:
            only_method_object += [method]
    return only_method_object


show_method(bool)
