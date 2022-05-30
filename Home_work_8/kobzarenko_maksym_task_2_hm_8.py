def max_number_from_two_arg(numbre_1: int, number_2: int):
    ''' Функция принимает 2 аргумента (int) и находить максимум из них '''
    return max(numbre_1, number_2)


print(max_number_from_two_arg(4, 5))


def max_number_from_three_arg(numbre_1: int, number_2: int, number_3: int):
    ''' Функция принимает 3 аргумента (int) и находить максимум из них. В начале сравниваем 2 первых аргумента с помощью
    функции max_number_from_two_arg, затем выод этой функции сравниваем с 3-м аргументом функции max_number_from_three_arg '''
    middle = max_number_from_two_arg(numbre_1, number_2)
    return max_number_from_two_arg(middle, number_3)


print(max_number_from_three_arg(4, 5, 9))
