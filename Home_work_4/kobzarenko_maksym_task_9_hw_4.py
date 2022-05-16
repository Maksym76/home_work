#  Создаем 2 переменные класса "list"
list_1 = [151, 235, 1, 36]
list_2 = [555, 1, 85, 36]

# Проверяем 2 списка на повторения елементов. Если хоть один элемент совпадает выводим "True"
for element in list_1:
    if element in list_2:
        print(element in list_2)
        break
