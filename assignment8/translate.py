import os.path
from os import path
import gtts


def read_from_file():
    global words_bank

    f = open("translate.txt", "r")
    
    temp = f.read().split("\n")
    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i + 1]}
        words_bank.append(my_dict)
    f.close()

def translate_english_to_persian():
    user_text = input("Enter your English text: ")
    user_words = user_text.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output= output + word["fa"] + " "
                break
        else:
            output=output + user_word + " "
    print(output)

    voice=gtts.gTTS(output,lang="en",slow=False)
    voice.save("Tvoice.mp3") 


def translate_persian_to_english():
    user_text = input("Enter your Persian text: ")
    user_words = user_text.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                output=output + word["en"] + " "
                break
        else:
            output= output + user_word + " "
    print(output)

def add_new_word():
    file_name ="translate.txt"
    if path.exists(file_name):
        d = open("translate.txt", "a")
        new_word_en = input("enter your English word: ")
        for word in words_bank:
            if new_word_en == word["en"]:
                print("This word is already exist in the database!! \n")
                break
        else:
            new_word_fa = input("enter word translation in Persian: ")
            d.write("\n" + new_word_en + "\n" + new_word_fa)
            print("New word added successfully. \n")
        d.close()
    else:
        print("File does not exist! \n")



def show_menu():
    print("Welcome to my translator")
    print("1 - Translate English to Persian")
    print("2 - Translate Persian to English")
    print("3 - Add a new word to the database")
    print("4 - Exit")


read_from_file()

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        translate_english_to_persian()
    if choice == 2:
        translate_persian_to_english()
    if choice == 3:
        add_new_word()
    if choice == 4:
        exit(0)
