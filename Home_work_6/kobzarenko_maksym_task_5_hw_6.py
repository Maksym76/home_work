list_dictionary: list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                         {"VIII": "S007"}]

#  Создаем объект (class set) c уникальными елементами взятые из значений словарей которые вложенные в список
#  переменной (list_dictionary).
value: set = set()

# Проходим по каждому словарю вложенного в список переменной (list_dictionary)
for dictionary in list_dictionary:
    # Добовляем в нашу переменную (value) значения из словарей (dictionary)
    value |= set(dictionary.values())

print(value)

# Создаем список в котором будут хранится словари из переменной (list_dictionary) с уникальными значениями.
dictionary_L: list = []

# Проходим по каждому словарю вложенного в список переменной (list_dictionary)
for dictionary_1 in list_dictionary:
    # Присваиваем ключ-значения из словаря переменным (key, value_1)
    for key, value_1 in dict(dictionary_1).items():
        # Проверяем есть ли значение в переменной (value). Если условие выполняется то делаем следующие действия
        if value_1 in value:
            # Добовляем в переменную (list_dictionary) словарь с уникальным значением
            dictionary_L.append({key: value_1})
            # Удоляем значение из переменной (value_1) для того что-бы небыло ключей с одиноковыми значениями
            value.discard(value_1)

print(dictionary_L)
