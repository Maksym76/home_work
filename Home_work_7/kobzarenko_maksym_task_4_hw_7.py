# Написать функцию которая принимает в качестве аргумента номер месяца, и возвращает строку - время года, этого месяца.

def season(number_month):
    if number_month <= 2 or number_month == 12:  # Если аргумент равен 1, 2 или 3. Выводим то что сейчас зима
         print('Winter season')
    elif 2 < number_month <= 5:  # Если аргумент равен 3, 4 или 5. Выводим то что сейчас весна
         print('Spring season')
    elif 5 < number_month <= 8:  # Если аргумент равен 6, 7 или 8. Выводим то что сейчас лето
         print('Summer season')
    elif 8 < number_month <= 11:  # Если аргумент равен 9, 10  или 11. Выводим то что сейчас осень
         print('Autumn season')


print(season(12))
