#  Импортируем библиотеку
import datetime

#  Создаем переменную в которой будет хранится текущая дата и время
now = datetime.datetime.now()

year = lambda x: x.year  # С помощью "lamda" функции будем возвращать текущий год из экземпляра класса "datetime"
month = lambda x: x.month  # С помощью "lamda" функции будем возвращать текущий месяц из экземпляра класса "datetime"
day = lambda x: x.day  # С помощью "lamda" функции будем возвращать текущий день из экземпляра класса "datetime"

print(year(now))

print(month(now))

print(day(now))
