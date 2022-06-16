# Создаем класс "Car" который будет иметь только один экземпляр класса. Для этого воспользуемся патерном "Singletone"
class Car():
    # Создаем частную переменную которая будет хранить только одну сылку на экземпляр класса
    __instance = None

    # Создаем экземпляр класса с помощью магического методы "__new__"
    def __new__(cls, *args, **kwargs):
        # Проверяем содержит ли наша переменная ссылку на экземпляр класса.
        if cls.__instance is None:  # Если переменна не содержит ссылку на экземпляр класса то мы создаем экземпляр
            # класса и возвращаем объект
            cls.__instance = super(Car, cls).__new__(cls)
        return cls.__instance  # Если переменна уже содержит ссылку на экземпляр класса то мы ее возвращаем

    # Пишем метод в котором будем инициализировать экземпляр класса "Car" и его атрибуты
    def __init__(self, color='white', complectation='basic', wheels_diametr=15):  # В именнованых аргументах указаны
        # атрибуты объекта по умолчанию их можно поменять на свои
        self.color = color
        self.complectation = complectation
        self.wheels_diametr = wheels_diametr

    # Метод показывает как создать объкт класса
    def __repr__(self):
        return '''При создании экземпляра класса (автомобиль) он изначально состоит из базовой комплектации(color='white', 
        complectation='basic', wheels_diametr=15). Но вы можете в аргументах указать свои опции которые будут применены 
        к вашему автомобилю. Вы можете выбрать: свой цвет, комплектацию и диаметр дисков. 
        Например: my_car = Car(color='red', complectation='elegand', wheels_diametr=18)'''

    # Метод будет выводить словарь с атрибутами экземпляра класса (возвращает словарь с выбранными опциями автомобиля)
    def __call__(self, *args, **kwargs):
        return vars(self)

    @property
    # Функця выводит текст с выбраными опциями для автомобиля
    def car_option(self):
        return f'''Вы выбрали следующие опции: color = {self.color}, complectation = {self.complectation},
               wheels_diametr = {self.wheels_diametr}'''

    @car_option.setter
    # Функция меняет локальные атрибуты экземпляра класса (меняет опции в автомобиле)
    def car_option(self, set_another_option: dict):
        if "color" in set_another_option.keys():
            self.color = set_another_option.get('color')
        elif "complectation" in set_another_option.keys():
            self.complectation = set_another_option.get("complectation")
        elif "wheels_diametr" in set_another_option.keys():
            self.wheels_diametr = set_another_option.get("wheels_diametr")
        else:
            raise Exception('Вы указали несущетвующей опции! \n Обратитесь к менеджеру за информацией')

    @car_option.deleter
    # Возвращает бозовые опции автомобиля
    def car_option(self):
        self.color = 'white'
        self.complectation = "basic"
        self.wheels_diametr = 15


my_car_1 = Car(color='black', complectation='super', wheels_diametr=18)  # Создаем экземпляр класса
print(my_car_1, end='\n\n\n')  # Выводим текст как создеётся экземпляр класса. Метод "__repr__" показывает как создать
# объкт класса

# Создаем переменную которая будет содержать словарь с атрибутами экземпляра класса (возвращает словарь с выбранными
# опциями автомобиля). С помощью метода "__call__"
car_option = my_car_1()
print(car_option, end='\n\n\n')

# Выводим текст в котором пишуться наши опции. Проверяем наш getter
print(my_car_1.car_option, end='\n\n\n')

# Меняем наши опции.  Проверяем наш setter
my_car_1.car_option = {"color": 'green'}
print(my_car_1.car_option, end='\n\n\n')

# Скидываем опции автомобиля до базовых. Проверяем наш deletter
del my_car_1.car_option
print(my_car_1.car_option, end='\n\n\n')

# Создаем еще один экземпляр класса для проверки того что наш класс "Car" может иметь только один экземпляр класса
my_car_2 = Car()
print(id(my_car_1), id(my_car_2))
