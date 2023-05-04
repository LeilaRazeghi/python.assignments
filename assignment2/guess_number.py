import random

computer_number=random.randint(10,40)
guess_no=0

for i in range(31):

    user_number=int(input())
    guess_no=guess_no+1

    if computer_number== user_number:
        print("excellent")
        print("you win")
        print("🎉")
        print("your guess number is:", guess_no)
        break
    
    elif computer_number>user_number:
        print("go up") 
        print("⬆")
    elif computer_number<user_number:
        print("go down")
        print("⬇")