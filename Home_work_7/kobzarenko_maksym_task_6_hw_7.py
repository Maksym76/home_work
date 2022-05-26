# Написать функцию которая принимает в качестве аргумента строку, и возвращает True, если строка является полиндромом и
# False если нет.

def polindro (text):
    if text == text[::-1]:
        return print(True)
    else:
        return print(False)

print(polindro("adad"))
