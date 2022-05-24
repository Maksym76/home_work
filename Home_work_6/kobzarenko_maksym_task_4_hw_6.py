dictionary: dict = {
    'id1': {'name': 'Ruslan',
            'class': 1,
            'subjects': {'Math', 'Algorithms', 'English'}
            },

    'id2': {'name': 'Mark',
            'class': 2,
            'subjects': {'Geometry', 'Java', 'Cooking'}
            },

    'id3': {'name': 'Ruslan',
            'class': 1,
            'subjects': {'Math', 'Algorithms', 'English'}
            }

}

# Создаем переменную класса лист. В эту переменную будем записывать уникальные "значения" из словаря переменной (dictionary)
values: list = list()
# Создаём новый словарь с уникальными "значениями".
new_dict: set = {}
# Проходим в переменной (dictionary) по всем ключ-значениям словаря.
for key, value in dictionary.items():
    # Если value(значения)  нету в нашей переменной (values), то мы её добовляем в неё. И записываем нащи key(ключ),
    # value(значение) в пременную (new_dict)
    if value not in values:
        new_dict.update({key: value})
        values.append(value)

print("Новый словарь без повторений", new_dict, sep='\n')
