import sys
import random

print('Welcome to The Office Name Picker!\n')
print('Here is your name:')

first = ('Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert')
last = ('Scott', 'Schrute', 'Halpert', 'Beesly',
        'Howard', 'Bernard', 'California')

while True:
    firstname = random.choice(first)
    lastname = random.choice(last)

    print(firstname, lastname, file=sys.stderr)

    try_again = input('\nTry Again? (Press Enter or x to quit)\n')

    if try_again.lower() == 'x':
        break

input('\nPress Enter to confirm exit')
