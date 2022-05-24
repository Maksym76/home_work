# Создаём пустой словарь
exemple_dict: dict = {}

#  Создать словарь с ключами от 11 до 20 включительно. Значения = квадраты ключей. Для этого с помощью цикла 'for' задаём
#  диапозон от 11 до 20
for i in range(11, 21):
    exemple_dict [i] = i**2

#  Суммируем все значение в словаре
sum_of_key: int = sum(exemple_dict.values())

print(exemple_dict)
print(f'Сумма всех значей в "exemple_dict" равна "{sum_of_key}"')

