#  Проверяем числа в диапозоне от -99 до 99 которые делятся на 3 без остатка.
for x in range(-99, 99, 3):
    if x % 3 == 0:
        print(f'это <<{x}>> делится без остатка на 3''')
