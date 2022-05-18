# Создаем переменну типа "список"
massif = []

# Добовляем в нашу переменную "massif" 5 списков, что-бы получить массив размером 5х5
for i in range(5):  #
    massif.append([' '] * 5)

# Выводим наш массив на экран с помощью цикла "for"
for i in range(4, -1, -1): # Отсчет строки (у) у нас идет с низу в верх
    for j in range(5): # Отсчет столбцов (х) идет с лева на право
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

    # Если пользователь выбрал "1" вариант
    if option == 1:
        # Просим пользователя ввести координаты (x=2;y=2;value='v'). Значения вводим (x,y,value) ТОЛЬКО числами через ";"
        coordinates = list(map(int, (input("Введите x и y в формате x=2;y=2;value='v': ").split(';'))))
        # Если ячейка не занята, программа делает запись в ячейку по введеным координатам
        if massif[coordinates[0]] [coordinates[1]] == ' ':
            massif[coordinates[0]] [coordinates[1]] = coordinates[2]
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
                        massif[coordinates[1]] [coordinates[0]] = coordinates[2]
                print('Запись сделана!')

            else:
                continue

    # Если пользователь выбрал "2" вариант
    elif option == 2:
        # Просим пользователя ввести координаты (x=2;y=2). Значения вводим ТОЛЬКО через числа разделенные ";"
        coordinates_2 = list(map(int, (input("Введите x и y в формате x=2;y=2: ").split(';'))))
        if massif[coordinates_2[0]] [coordinates_2[1]] == ' ':
            print("Пустая ячейка")
            continue
        else:
            print(massif[coordinates_2[0]] [coordinates_2[1]])


    # elif option == 3:
    #     print()
    # elif option == 4:
    #     print()
    # elif option == 0:
    #     print()

    # print(massif)
    for i in range(4, -1, -1): # Строка
        for j in range(5): # Столбец
            print(massif[i][j], end='|')
        print()
    #










    # for i in range(x3_1[0]):
    #     for j in range(x3_1[1]):
    #         if x[i][j] == ' ':
    #             x[i][j].replace(' ', str(x3_1[2]))

