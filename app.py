from time import sleep
import game
import sys

print("Welcome to jokenpo!")
sleep(2)
while True:
    d1 = input("Let's play? Answer with 1/Yes or 0/No to continue: ")
    d1.strip().lower()
    if d1 == "yes" or d1 == "1" or d1 == "y":
        game.play()
    elif d1 == "no" or d1 == "0" or d1 == "n":
        print("Thank You!")
        sys.exit()
    else:
        print("Wrong answer!")
