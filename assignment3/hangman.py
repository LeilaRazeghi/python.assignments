import random

words_bank=["tree","book","blue","train","fish","woman","life","freedom","iran","sky"]
user_mistakes=0

good_chars=[]
bad_chars=[]

x=random.randint(0, len(words_bank)-1)

word=words_bank[x]
while user_mistakes<6:
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")
        else:
            print("-", end=" ")
    if len(word)==len(good_chars):
        print("you win")
        print("👏")
        break

    user_char=input("please write your guess:").lower()
    if len(user_char)==1:
        if user_char in word:
            good_chars.append(user_char)
            print("✔")
        else:
            bad_chars.append(user_char)
            user_mistakes =+1
            print("❌")
    else:
        print("enter word's length correctly")      
if user_mistakes==6:
    print("game over 💀 ")  