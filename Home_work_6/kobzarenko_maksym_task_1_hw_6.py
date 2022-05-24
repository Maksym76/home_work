first: dict = {1: 10, 2: 20}

second: dict = {3: 30, 4: 40}

third: dict = {5: 50, 6: 60}

fourth: dict = {7: 70, 8: 80}

fifth: dict = {9: 90, 10: 100}

# Создаем новый словарь куда будем добовлять выше перечисленые словари
summed_sets: dict = {}

# С помощью цикла 'for' с  существующего словаря добовляем (ключь: значения) в наш новый словарь(summed_sets). Повторяем
# так для каждого существующего словоря
for key, value in first.items():
    summed_sets [key] = value

for key, value in second.items():
    summed_sets [key] = value

for key, value in third.items():
    summed_sets [key] = value

for key, value in fourth.items():
    summed_sets [key] = value

for key, value in fifth.items():
    summed_sets [key] = value

print(summed_sets)

