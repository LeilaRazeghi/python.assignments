import pyfiglet
from termcolor import colored
import random
import time

def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print( )

def menu():
    print("1-Two player.")
    print("2-One Player and PC.")
    print("3-Exit.") 

  #GB=game_board
def check_game_1(GB):
        if GB[0][0] == GB[0][1] == GB[0][2] == (colored("X", "red")) or GB[1][0] == GB[1][1] == GB[1][2] == (colored("X", "red")) or GB[2][0] == GB[2][1] == GB[2][2] == (colored("X", "red")) or GB[0][0] == GB[1][0] == GB[2][0] == (colored("X", "red")) or GB[0][1] == GB[1][1] == GB[2][1] == (colored("X", "red")) or GB[0][2] == GB[1][2] == GB[2][2] == (colored("X", "red")) or GB[0][0] == GB[1][1] == GB[2][2] == (colored("X", "red")) or GB[0][2] == GB[1][1] == GB[2][0] == (colored("X", "red")):
            print("player 1 winns")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)
        elif GB[0][0] == GB[0][1] == GB[0][2] == (colored("O", "blue")) or GB[1][0] == GB[1][1] == GB[1][2] == (colored("O", "blue")) or GB[2][0] == GB[2][1] == GB[2][2] == (colored("O", "blue")) or GB[0][0] == GB[1][0] == GB[2][0] == (colored("O", "blue")) or GB[0][1] == GB[1][1] == GB[2][1] == (colored("O", "blue")) or GB[0][2] == GB[1][2] == GB[2][2] == (colored("O", "blue")) or GB[0][0] == GB[1][1] == GB[2][2] == (colored("O", "blue")) or GB[0][2] == GB[1][1] == GB[2][0] == (colored("O", "blue")):
            print("player 2 winns")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)
        elif GB[0][0]!= "_" and GB[0][1]!= "_" and GB[0][2]!= "_" and GB[1][0]!= "_" and GB[1][1]!= "_" and GB[1][2]!= "_" and GB[2][0]!= "_" and GB[2][1]!= "_" and GB[2][2] != "_":
            print("draw! no one winns!")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)

def check_game_2(GB):
        if GB[0][0] == GB[0][1] == GB[0][2] == (colored("X", "red")) or GB[1][0] == GB[1][1] == GB[1][2] == (colored("X", "red")) or GB[2][0] == GB[2][1] == GB[2][2] == (colored("X", "red")) or GB[0][0] == GB[1][0] == GB[2][0] == (colored("X", "red")) or GB[0][1] == GB[1][1] == GB[2][1] == (colored("X", "red")) or GB[0][2] == GB[1][2] == GB[2][2] == (colored("X", "red")) or GB[0][0] == GB[1][1] == GB[2][2] == (colored("X", "red")) or GB[0][2] == GB[1][1] == GB[2][0] == (colored("X", "red")):
            print("you winned")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)
        elif GB[0][0] == GB[0][1] == GB[0][2] == (colored("O", "blue")) or GB[1][0] == GB[1][1] == GB[1][2] == (colored("O", "blue")) or GB[2][0] == GB[2][1] == GB[2][2] == (colored("O", "blue")) or GB[0][0] == GB[1][0] == GB[2][0] == (colored("O", "blue")) or GB[0][1] == GB[1][1] == GB[2][1] == (colored("O", "blue")) or GB[0][2] == GB[1][2] == GB[2][2] == (colored("O", "blue")) or GB[0][0] == GB[1][1] == GB[2][2] == (colored("O", "blue")) or GB[0][2] == GB[1][1] == GB[2][0] == (colored("O", "blue")):
            print("PC winned")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)
        elif GB[0][0]!= "_" and GB[0][1]!= "_" and GB[0][2]!= "_" and GB[1][0]!= "_" and GB[1][1]!= "_" and GB[1][2]!= "_" and GB[2][0]!= "_" and GB[2][1]!= "_" and GB[2][2] != "_":
            print("draw! no one winned")
            end = time.time()
            d=int(end-start)
            print("Duration:", d ,"second")
            exit(0)


title = pyfiglet.figlet_format("TicTacToe" , font = "slant")
print(title)

while True:
    menu()
    choice=int(input("Please enter your choice:"))
    start = time.time()

    if choice == 1:
        game_board = [["_", "_", "_"],
                      ["_", "_", "_"],
                      ["_", "_", "_"]]

        show()
        while True:
            print("Player1: ")

            while True :
                row = int(input("row: "))
                col = int (input("column : "))
                if 0<=row<=2 and 0<=col<=2 :
                    if game_board[row][col] == "_":
                        game_board[row][col] = (colored("X", "red"))
                        break
                    else :
                     print("Incorrect choice! you should select empty place:")
                else :
                    print ("Invalid input! You can only choose 0 or 1 or 2.")

            show()
            check_game_1(game_board)

            print("Player2: ")
            while True :
                row = int(input("row: "))
                col = int (input("column : "))
                if 0<=row<=2 and 0<=col<=2 :
                    if game_board[row][col] == "_":
                        game_board[row][col] = (colored("O", "blue"))
                        break
                    else :
                        print("Incorrect choice!you should select empty place :")
                else :
                    print ("Invalid input! You can only choose 0 or 1 or 2.")
            show()
            check_game_1(game_board)


    elif choice == 2:
        game_board = [["_", "_", "_"],
                      ["_", "_", "_"],
                      ["_", "_", "_"]]

        show()
        while True:
            print("Your turn: ")

            while True :
                row=int(input("row : "))
                col=int (input("column : "))
                if 0<=row<=2 and 0<=col<=2 :
                    if game_board[row][col] == "_":
                        game_board[row][col] = (colored("X", "red"))
                        break
                    else :
                     print("Incorrect choice! you should select empty place:")
                else :
                    print ("Invalid input! You can only choose 0 or 1 or 2.")

            show()
            check_game_2(game_board)

            print("PC:")
            while True :
                raw=random.randint(0, 2)
                col=random.randint(0, 2)
                if game_board[col][row] == "_":
                    game_board[col][row] = (colored("O", "blue"))
                    break
                else:
                    continue
            show()
            check_game_2(game_board)

    elif choice == 3:
        exit(0)
    else:
        print("Wrong choice! you should select option 1 or 2 or 3")