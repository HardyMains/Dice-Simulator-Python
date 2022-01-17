import random, sys
ask = input('Are you sure, You want to roll the dice - y/n : ')
if ask == 'y':
    roll_dice = random.randint(1,6)
    print(roll_dice)
    while True:
        ask_againa = input('Want to roll one more time? - y/n: ')
        if ask_againa == 'y':
            roll_dice = random.randint(1,6)
            print(roll_dice)
        elif ask_againa == 'n':
            sys.exit()
        
elif ask == 'n':
    sys.exit()
else:
    ask = input('Are you sure, You want to roll the dice - y/n : ')
    while True:
        if ask == 'y':
            z = random.randint(1,6)
            print(z)
            ask = input('Want to roll one more time - y/n : ')
        elif ask == 'n':
            sys.exit()
        else:
            ask = input('Are you sure, You want to roll the dice - y/n : ')