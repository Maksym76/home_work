#  Пример списка
input = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]

# ВАРИАНТ 1: Можем отсортировать с помощью метода колекции лист, при этом измениться наш "пример списка". Отсортировать
# наш список с кортежами по возрастанию чисел которые находятся в кортеже

input.sort(key=lambda element: element[1])  # В метод нашего списка, в значение "key" мы прописываем "lambda" в которой
# мы берем второй елемент нашего кортежа (то есть число находящиеся в кортеже) и по этому числу мы сортируем наш список
# по возрастанию

# ВАРИАНТ 2 : Можем создать новую переменную. И с помощью функции "sorted" отсортировать наш список с кортежами
# по возрастанию чисел которые находятся в кортеже

output = sorted(input, key=lambda element: element[1])  # В метод нашего списка, в значение "key" мы прописываем "lambda"
# в которой мы берем второй елемент нашего кортежа (то есть число находящиеся в кортеже) и по этому числу мы сортируем
# наш список по возрастанию

print(input)

print(output)
