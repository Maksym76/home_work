'''Создать класс с методом которого можно будет возвращать область видимости (local) созданного экземпляра класса.
В конструкторе(__init__) вашего класса пускай будут те параметры которые вы захотите.'''


# Создаем класс "Car"
class Car():

    #  Пишем метод в котором будем инициализировать экземпляр класса "Car" и его атрибуты
    def __init__(self, color='white', complectation='basic', wheels_diametr=15):  # В именнованых аргументах указаны
        # атрибуты объекта по умолчанию их можно поменять на свои
        self.color = color
        self.complectation = complectation
        self.wheels_diametr = wheels_diametr

    # Метод который возвращает атрибуты объекта в виде словаря
    def object_local_atribut(self):
        return vars(self)


my_car = Car(color='black', complectation='super', wheels_diametr=18)
print(my_car.object_local_atribut())
