''' написать функцию которая с помощью assert будет тестировать ваш самописный reduce'''


def my_reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


# Создаем функцию которая будет тестировать функцию "my_reduce" с помощью "assert".
def test_reduce(function, iterable, initializer=None):
    assert len(iterable) != 0, 'Итерабельный объект в аргументе не должен быть пустым.'  # Пока условие "assert"
    # равняеться истине, ошибки не будет
    x = my_reduce(function, iterable, initializer)
    return x


print(test_reduce(lambda a, b: a + b, (1, 2, 3, 5, 8), 10))
