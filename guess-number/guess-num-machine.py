# guess-num-machine.py
# program for guessing the number machine

import random

def guess_num_mach(upper_limit):
    lower_limit = 1
    user_response = ''
    while user_response != 'C':
        gen_num = random.randint(lower_limit,upper_limit)
        user_response = input(f'Is {gen_num} too High (h), too Low (l) or correct (c): ').upper()
        if user_response == 'H':
            upper_limit = gen_num - 1
        elif user_response == 'L':
            lower_limit = gen_num + 1
    print(f'{gen_num} is correct ! Machine guessed it..')


upper_limit = int(input('Enter the upper limit: '))
x = input(f'Think of a number between 1 and {upper_limit} and press enter when ready..')
guess_num_mach(upper_limit)