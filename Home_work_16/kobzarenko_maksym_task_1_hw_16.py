import random

game: tuple = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')

while True:

    players_choice: str = input('Your choice (rock, paper, scissors, lizard, spock)? ').capitalize().lstrip().rstrip()

    computers_choice = random.choice(game)

    if players_choice not in game:
        print(f'Invalid input "{players_choice}"')
        continue

    elif players_choice == 'Scissors':
        if computers_choice == players_choice:
            print('Draw!')
        elif computers_choice == 'Lizard' or computers_choice == 'Paper':
            print("Pleyer win!")
        else:
            print('Computer win!')

    elif players_choice == 'Rock':
        if computers_choice == players_choice:
            print('Draw!')
        elif computers_choice == 'Lizard' or computers_choice == 'Scissors':
            print("Pleyer win!")
        else:
            print('Computer win!')

    elif players_choice == 'Paper':
        if computers_choice == players_choice:
            print('Draw!')
        elif computers_choice == 'Rock' or computers_choice == 'Spock':
            print("Pleyer win!")
        else:
            print('Computer win!')

    elif players_choice == 'Lizard':
        if computers_choice == players_choice:
            print('Draw!')
        elif computers_choice == 'Paper' or computers_choice == 'Spock':
            print("Pleyer win!")
        else:
            print('Computer win!')


    elif players_choice == 'Spock':
        if computers_choice == players_choice:
            print('Draw!')
        elif computers_choice == 'Scissors' or computers_choice == 'Rock':
            print("Pleyer win!")
        else:
            print('Computer win!')


    question_for_player = input('Repeat (Y/N)').upper()


    while question_for_player != 'Y' and question_for_player != 'N':
        print(f'Invalid input "{question_for_player}"')
        question_for_player = input('Repeat (Y/N)').upper()

    if question_for_player == 'Y':
        continue
    elif question_for_player == 'N':
        break
