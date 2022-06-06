#  Создаем функцию которая будет добовлять код страны к номеру телефона с помощью замыкания
def cod_country(cod_country: str):
    cod_country: str = cod_country  # В этой переменной будет указан код страны

    # Создаем функцию которая будет добовлять к нашему номеру код страны
    def cod_and_number(number: str):
        print(cod_country + number)  # Замыкаем нашу функцию и выводим телефон с кодом страны

    return cod_and_number


my_number = cod_country('+044')
my_number('838372893')
