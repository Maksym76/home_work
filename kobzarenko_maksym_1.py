# Ask user age
user_name: str = input('How old are you: ')

# If user write letter, say him write number
if user_name.isalpha():
    print('please write number')

# If user write number, we change type of variable from str to int
elif user_name.isdigit():
    user_name: int = int(user_name)

    # if user's age 21, write (You should visit Holland.)
    if user_name == 21:
        print('You should visit Holland.')
    # if user's age more than 21, write (You should visit Vietnam.)
    elif user_name > 21:
        print('You should visit Vietnam.')
    # if the upper conditions are not met, write (Travell everywhere)
    else:
        print('Travell everywhere')
