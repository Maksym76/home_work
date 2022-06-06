# C помощью магического метода __clouser__ мы можем c глобальной области вилимости достучаться до локальных переменных
# функции, которые были замкнуты. Замыкание функции - это когда локальные переменные функции используються внутри тела
# вложенной функции

def func():
    x: list = [3, 4, 4, 5, 6]
    y: list = ['qwerty']
    r: int = 2

    def some_func():
        print(r)
        print(x)
        print(y)

    print(r)
    return some_func


f = func()
print(f.__closure__[0].cell_contents)
print(f.__closure__[1].cell_contents)
print(f.__closure__[2].cell_contents)
print(f.__closure__)
