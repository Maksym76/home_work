import random

game: tuple = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')

while True:
    user_choice: str = input('''Make your choice:
    1) Rock
    2) Paper
    3) Scissors
    4) Lizard
    5) Spock 
    ''').capitalize().lstrip().rstrip()

    program_choice = random.choice(game)
    print(program_choice)

    if user_choice == 'Scissors' and (program_choice == 'Lizard' or 'Paper' or 'Scissors'):
        if program_choice == 'Scissors':
            print('Draw!')
            continue
        print('Congratulation! You win!')

    elif (user_choice == 'Rock') and (program_choice == 'Lizard' or 'Scissors' or 'Rock'):
        if program_choice == 'Rock':
            print('Draw!')
            continue
        print('Congratulation! You win!')

    elif (user_choice == 'Paper') and (program_choice == "Rock" or 'Spock' or 'Paper'):
        if program_choice == 'Paper':
            print('Draw!')
            continue
        print('Congratulation! You win!')

    elif (user_choice == 'Lizard') and (program_choice == "Paper" or 'Spock' or 'Lizard'):
        if program_choice == 'Lizard':
            print('Draw!')
            continue
        print('Congratulation! You win!')

    elif (user_choice == 'Spock') and (program_choice == 'Scissors' or 'Rock' or 'Spock'):
        if program_choice == 'Spock':
            print('Draw!')
            continue
        print('Congratulation! You win!')

    else:
        print('You lose!')

