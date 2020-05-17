import random
oneToNine = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:
    which = input('Type a number from 1 to 9. ') 
    compu = print(random.choice(oneToNine))
    if which == compu:
        print('You WIN!')
    else:
        print('You LOSE!')
