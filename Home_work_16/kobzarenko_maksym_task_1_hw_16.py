import random

game: tuple = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')

while True:
    user_choice: str = input('''Write full name your choice:
    1) Rock
    2) Paper
    3) Scissors
    4) Lizard
    5) Spock 
    ''').capitalize().lstrip().rstrip()

    program_choice = random.choice(game)

    if user_choice == 'Scissors':
        if program_choice == user_choice:
            print('Draw!')
        elif program_choice == 'Lizard' or program_choice == 'Paper':
            print("Congratulations! You win! ")
        else:
            print('You lose!')

    elif user_choice == 'Rock':
        if program_choice == user_choice:
            print('Draw!')
        elif program_choice == 'Lizard' or program_choice == 'Scissors':
            print("Congratulations! You win! ")
        else:
            print('You lose!')

    elif user_choice == 'Paper':
        if program_choice == user_choice:
            print('Draw!')
        elif program_choice == 'Rock' or program_choice == 'Spock':
            print("Congratulations! You win!")
        else:
            print('You lose!')

    elif user_choice == 'Lizard':
        if program_choice == user_choice:
            print('Draw!')
        elif program_choice == 'Paper' or program_choice == 'Spock':
            print("Congratulations! You win!")
        else:
            print('You lose!')


    elif user_choice == 'Spock':
        if program_choice == user_choice:
            print('Draw!')
        elif program_choice == 'Scissors' or program_choice == 'Rock':
            print("Congratulations! You win!")
        else:
            print('You lose!')

    question_for_user = input('''Do you want start again (write number of answer)?
     1) Yes
     2) No
     ''')

    if question_for_user == '1':
        continue
    else:
        break
