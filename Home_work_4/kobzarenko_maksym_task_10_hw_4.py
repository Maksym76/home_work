x = []

for i in range(5):
    x.append([' '] * 5)

for i in range(5):
    for j in range(5):
        print(x[i][j], end='|')
    print()

option = int(input('''Выбери действие:

1) Сделать запись

2) Получить значение по координатам

3) Показать все ячейки

4) Удалить значение по координатам

0) Программа завершает работу.

'''))

if option == 1:
    x3_1 = list(map(int, (input("Введите x и y в формате x=2;y=2;value='v': ").split(';'))))
    if x[x3_1[0]][x3_1[1]] == ' ':
        x[x3_1[0]][x3_1[1]].replace(' ', str(x3_1[2]))
        print(x)










    # for i in range(x3_1[0]):
    #     for j in range(x3_1[1]):
    #         if x[i][j] == ' ':
    #             x[i][j].replace(' ', str(x3_1[2]))

