# Создаем дэкоратор в котором будет выводиться колличество методов объекта
def decore_amound_method(func):
    def wrapper(object):
        mount_method: int = len(func(object))  # Считаем колличество методов для данного объкта. Список методов берем из
        # вложенной функции в дэкораторе
        print(func(object), f'Колличество методов в объекте = {mount_method}шт.', sep='\n')

    return wrapper


@decore_amound_method
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
