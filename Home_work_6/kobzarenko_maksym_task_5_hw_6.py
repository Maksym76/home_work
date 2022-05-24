list_dictionary: list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                         {"VIII": "S007"}]

#  Создаем объект (class set). В него будем записывать значения словарей вложенных в спивок переменной (list_dictionary)
value: set = set()

# Проходим по каждому словарю вложенного в список
for dictionary in list_dictionary:
    # Добовляем в нашу переменную (value) значения из словарей (dictionary)
    value |= set(dictionary.values())

print(value)  # {'S007', 'S009', 'S002', 'S005', 'S001'}
