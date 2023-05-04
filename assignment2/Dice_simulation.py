import random

for i in range(1, 7):
    dice_result=random.randint(1, 6)
    print(dice_result)

    if dice_result==6:
        print("congratulation👏 you can throw the dice again")
    else:
        dice_result=random.randint(1,6)
        print(dice_result)
        break