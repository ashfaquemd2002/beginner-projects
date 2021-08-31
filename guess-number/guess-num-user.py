# guess-num-user.py
# program for guessing number by user

import random

def guess_num_user(upper_limit):
    gen_num = random.randint(1,upper_limit)
    user_num = 0
    while user_num != gen_num:
        user_num = int(input(f'Guess the number between 1 and {upper_limit}: '))
        if user_num > gen_num:
            print('Too High !')
        elif user_num < gen_num:
            print('Too Low !')
    print('You guessed right !!')


upper_limit = int(input('Enter the upper limit number: '))
guess_num_user(upper_limit)