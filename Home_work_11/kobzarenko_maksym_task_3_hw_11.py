# Функции которая делит первый аргумент на второй
def func_division(arg_1: int, arg_2: int):
    try:
        result = arg_1 / arg_2  # Делим первый аргумент на второй
        print(f'Result of computation = {result}')
        return result
    except ZeroDivisionError:  # Если мы в условии нашей функции делим на ноль, то мы ловим ошибку "ZeroDivisionError".
        # и пишем следующий текст
        print("ай яй яй делить на ноль можно не многим")
    except BaseException as errore:  # Если ловим какие небудь другие исключения то выводим название этого исключения в
        # виде текста
        print(f'Вы споймали ошибку: {errore}')
    finally:  # И в конце в любых случаях выводим следующий текст
        print(" I 'am happy that you learn python")


func_division(1, 1)
