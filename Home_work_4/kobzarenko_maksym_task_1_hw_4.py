# Вводим текст
text = input("Write text: ")

# Если длина текста меньше 3 элементов выводи 'Ваша (text) слишком короткая'
if len(text) < 3:
    print('Ваша %s слишком короткая' % 'строка')
# Выводим первые и последнии 2 буквы слова
else:
    print(text[0:2] + text[-1:-3:-1])