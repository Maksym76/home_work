nickname_user: str = input('type your nikename: ')  # ask user's name

gender_user: str = input('type your gender (male or female): ')  # ask user's gender

age_user: int = int(input('type your age: '))  # ask user's age

# if user's name is 'admin', we greet user "Привет, повелитель!" and proceeding from age and gender we do offer
if nickname_user == 'admin':
    print("Привет, повелитель!", )
    if (10 < age_user < 14 and gender_user == 'male') or (age_user > 30 and gender_user == 'male'):
        print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'")
    elif 22 < age_user < 32 and gender_user == 'female':
        print("Советую Вам посмотреть 'Трансформеры'")
    elif age_user < 16 and gender_user == 'female':
        print("Советую Вам посмотреть 'Инсургент'")
    elif age_user < 12 and gender_user == 'male':
        print("Советую Вам посмотреть 'TMNT'")

# if user's name is 'Женя' we just do only one offer
elif nickname_user == 'Женя':
    print("Советую Вам посмотреть 'Дурак'")

# if user's name is 'Guido' we add 'Огромное спасибо!' to our offer proceeding from age and gender
elif nickname_user == 'Guido':

    if (10 < age_user < 14 and gender_user == 'male') or (age_user > 30 and gender_user == 'male'):
        print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'. " + 'Огромное спасибо!')
    elif 22 < age_user < 32 and gender_user == 'female':
        print("Советую Вам посмотреть 'Трансформеры'." + "Огромное спасибо!")
    elif age_user < 16 and gender_user == 'female':
        print("Советую Вам посмотреть 'Инсургент'." + "Огромное спасибо!")
    elif age_user < 12 and gender_user == 'male':
        print("Советую Вам посмотреть 'TMNT'." + "Огромное спасибо!")

# if the names do not match the above we do  proceeding from age and gender
else:
    print('Привет, ' + nickname_user + '!')

    if (10 < age_user < 14 and gender_user == 'male') or (age_user > 30 and gender_user == 'male'):
        print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'")
    elif 22 < age_user < 32 and gender_user == 'female':
        print("Советую Вам посмотреть 'Трансформеры'")
    elif age_user < 16 and gender_user == 'female':
        print("Советую Вам посмотреть 'Инсургент'")
    elif age_user < 12 and gender_user == 'male':
        print("Советую Вам посмотреть 'TMNT'")
