import random

money = 15

while money > 0:
    dice1 = random.randint(1, 6)
    print(dice1)

    dice2 = random.randint(1, 6)
    print(dice2)

    outcome = dice1 + dice2
    print(outcome)

