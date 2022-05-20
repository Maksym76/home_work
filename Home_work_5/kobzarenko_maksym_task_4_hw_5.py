list_set_method: list = dir(set)  # Создаем лист с методами принадлежащие к "set"
exception: list = []  # Создаем счетчик в котором будем записывать какие методы мы будем удалять из нашего списка

for method in list_set_method:  # Проходим по всем методам нашего списка
    if '_' in method:  # Ищем методы которые имеют в названии "_"
        exception += [method]  # Добовляем к нашим исключениям метод если он содержит в своем названии "_"


for del_method in exception:  # Берем каждый  метод из "еxception"
    if del_method in list_set_method:  # Если метод из "del_method" есть в "list_set_method". Мы его удаляем.
        list_set_method.remove(del_method)  # Удоляем метод из списка "list_set_method"

print(list_set_method)
