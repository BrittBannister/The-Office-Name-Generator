'''Generates names by randomly combining names from two seperate lists.'''
import sys
import random


def main():
    '''Selects names at random from two lists and combines them.'''
    print('Welcome to The Office Name Picker!\n')
    print('Here is your name:')

    first = ('Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert')
    last = ('Scott', 'Schrute', 'Halpert', 'Beesly',
            'Howard', 'Bernard', 'California')

    while True:
        firstname = random.choice(first)
        lastname = random.choice(last)

        print(firstname, lastname, file=sys.stderr)

        try_again = input(
            '\nTry Again? (Press Enter or x (then enter) to quit)\n')

        if try_again.lower() == 'x':
            break

    input('\nPress Enter to confirm exit')


if __name__ == '__main__':
    main()
