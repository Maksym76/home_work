exemple_set_1: set = {1, 2, 3, 4, 5, 6, 7, 8}  # Премир нашего множества
exemple_set_2: set = {8, 9, 10, 11, 12}  # Премир нашего множества

exemple_set_1.isdisjoint([9, 2, 3])  # истина (True), если set и other не имеют общих элементов.
exemple_set_1.remove(4)  # удаляет элемент из множества. KeyError, если такого элемента не существует
exemple_set_1.discard()  # yдаляет элемент. Если его не было, ошибка не возникает
exemple_set_1.pop()  # удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой
# элемент будет первым.
exemple_set_1.add(5)  # добавляет элемент в множество.
exemple_set_1.copy()  # копия множества.
exemple_set_1.difference(exemple_set_2)  # разность множеств. Возвращает новый объект.
exemple_set_1.difference_update(exemple_set_2)  # разность множеств. Удаляет все элементы кроме разности елементов в
                                                # множестве для которго вызывается меод
exemple_set_1.intersection(exemple_set_2)  # пересечение множеств.Возвращает новый объект.
exemple_set_1.intersection_update()  # пересечение множеств.Перезаписывает вызываемое множество
exemple_set_1.issubset()  # возвращет True, если все элементы множества для которого вызывается метод, содержаться в
                          # множестве-аргументе
exemple_set_1.issuperset()   # возвращет True, если все элементы множества-аргумента содержаться в множестве для котороо
                             # вызывается метод
exemple_set_1.symmetric_difference() # множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
                                     # Возвращает новый объект.
exemple_set_1.symmetric_difference_update()  # множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
                                             # Перезаписывает вызываемое множество
exemple_set_1.union(exemple_set_2)  # объеденение множеств. Возвращает новый объект.
exemple_set_1.update()  # Добавляет все элементы множества-аргумента(итерабельный объект) к множеству для которго вызывается метод
exemple_set_1.clear()  # очистка множества.