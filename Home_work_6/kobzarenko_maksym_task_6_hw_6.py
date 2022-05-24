# Посчитать общее количество наименований в СПИСКЕ. И только в СПИСКАХ.

shedule: dict = {
    'monday': ['clean house', 'drive car', 'meet with freands'],
    'thuesday': None,
    'wednesday': ['manicure', 'hammam', 'beer']
}

# Записываем все наши ключи из словаря в нову переменную класса (лист)
key_shedule: list = list(shedule.values())
#  Создаем счетчик куда мы будем записывать колличество елементов находящихся в списках которые вложены в список
#  переменной (key_shedule)
counter: int = 0
# Проходим по каждому элементу списка (key_shedule)
for elements in key_shedule:
    # Если елемент является списковым литералом то мы считаем длину этого списка. И колличество элементов этого списка
    # добовляем в нашу переменную (counter)
    if isinstance(elements, list):
        counter += len(elements)

print(counter)
