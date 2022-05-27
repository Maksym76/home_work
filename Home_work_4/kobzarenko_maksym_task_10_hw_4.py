# Создаем переменну типа "список"
massif = []

# Добовляем в нашу переменную "massif" 5 списков, что-бы получить массив размером 5х5
for i in range(5):  #
    massif.append([' '] * 5)

# Выводим наш массив на экран с помощью цикла "for"
for i in range(4, -1, -1):  # Отсчет строки (ось у) у нас идет с низу в верх
    for j in range(5):  # Отсчет столбцов (ось х) идет с лева на право
        print(massif[i][j], end='|')  # разделяем наши ячейки массива знаком "|"
    print()

# запускаем наш цикл "while"
while True:

    # запрашиваем у пользователя выбрать одно из действий
    option = int(input('''Выбери действие:
    
    1) Сделать запись
    
    2) Получить значение по координатам
    
    3) Показать все ячейки
    
    4) Удалить значение по координатам
    
    0) Программа завершает работу.
    
    '''))

    # Если пользователь выбрал "1" вариант. Записываем или перезаписываем значение в ячейке
    if option == 1:
        # Просим пользователя ввести координаты (у=2;х=2;value='v'). Значения вводим (у,х,value) ТОЛЬКО числами через ";"
        coordinates = list(map(int, (input("Введите у и х в формате у=2;х=2;value='v': ").split(';'))))
        # Если ячейка не занята, программа делает запись в ячейку по введеным координатам
        if massif[coordinates[0]][coordinates[1]] == ' ':
            massif[coordinates[0]][coordinates[1]] = coordinates[2]
            print('Запись сделана!')
        # Если ячейка по введеным координатам занята, программа выводит "Ячейка занята! Перезаписать?: Да, Нет"
        else:
            print('''Ячейка занята! Перезаписать?
            1) Да.
            2) НЕТ!''')
            # Принимаем ответ пользователя
            answer = int(input())
            # Если пользователь выбрал "1" вариант мы меняем значение в ячейке на новое
            if answer == 1:
                for i in massif[coordinates[1]]:
                    for j in massif[coordinates[0]]:
                        massif[coordinates[1]][coordinates[0]] = coordinates[2]
                print('Запись сделана!')

            else:
                continue

    # Если пользователь выбрал "2" вариант. Выводим значение которое в ячейке
    elif option == 2:
        # Просим пользователя ввести координаты (у=2;х=2). Значения вводим ТОЛЬКО через числа разделенные ";"
        coordinates_2 = list(map(int, (input("Введите у и х в формате у=2;х=2: ").split(';'))))
        # Проверяем что находиться в ячейке, если пусто ты пишем "Пустая ячейка"
        if massif[coordinates_2[0]][coordinates_2[1]] == ' ':
            print("Пустая ячейка")
            continue
        # Выводим значение которое в ячейке
        else:
            print(massif[coordinates_2[0]][coordinates_2[1]])

    # Если пользователь выбрал "3" вариант. Выводим двухмерный масив со значениями которые там есть
    elif option == 3:
        # Выводим двухмерный массив со значениями на экран. И возвращаемся к выбору опций
        for i in range(4, -1, -1):  # Отсчет строки (ось у) у нас идет с низу в верх
            for j in range(5):  # Отсчет столбцов (ось х) идет с лева на право
                print(massif[i][j], end='|')  # разделяем наши ячейки массива знаком "|"
            print()
            continue

    # Если пользователь выбрал "4" вариант. Программа удоляет по введеным координатам значение в ячейке
    elif option == 4:
        # Просим пользователя ввести координаты (у=2;х=2). Значения вводим ТОЛЬКО через числа разделенные ";"
        coordinates_4 = list(map(int, (input("Введите у и х в формате у=2;х=2: ").split(';'))))
        # Если ячейка занята, то удаляем значение в этой ячейке и выводим на экран 'Запись удалена!'
        if massif[coordinates_4[0]][coordinates_4[1]] != ' ':
            massif[coordinates_4[0]][coordinates_4[1]] = ' '
            print('Запись удалена!')
        # Если ячейка пустая то возвращаемся к выбору опций
        else:
            continue

    # Если пользователь выбрал "0" вариант. Закрываем программу
    elif option == 0:
        break

#  чтобы в коде указвать значения по порядку (х,у), нужно цикл "for...in range..." поменять местами нижний цикл переместить на верх, а верхний в низ