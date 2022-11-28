import random


def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)

    sum_ = die1 + die2
    print(f'Player rolled {die1} + {die2} = {sum_}')

    return sum_


def chatter():
    chatters = random.randrange(1, 4)

    if chatters == 1:
        print("Oh, you're going for broke, huh?")
    elif chatters == 2:
        print("Aw c'mon, take a chance!")
    elif chatters == 3:
        print("You're up big. Now's the time to cash in your chips")

    return chatters


bank_balance = 1000

wager = int(input('Enter a wager: '))

while wager > bank_balance:
    wager = int(input('Enter a wager less or equal to the bank balance: '))

sum_of_dice = roll_dice()
chatter()
if sum_of_dice in (7, 11):
    game_status = 'WON'

elif sum_of_dice in (2, 3, 12):
    game_status = 'LOST'

else:
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print('Point is', my_point)

while game_status == 'CONTINUE':

    sum_of_dice = roll_dice()

    if sum_of_dice == my_point:
        game_status = 'WON'

    elif sum_of_dice == 7:
        game_status = 'LOST'

if game_status == 'WON':
    print('Player wins')
    bank_balance += wager
    print('Your bank balance is', bank_balance)
else:
    print('Player loses')
    bank_balance -= wager
    print('Your bank balance is', bank_balance)
