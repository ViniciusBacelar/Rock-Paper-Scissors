from random import randint
from time import sleep
import os
import sys


def play():
    scoreboard_computer = 0
    scoreboard_user = 0
    while True:
        computer = randint(0, 2)
        print('Your actions are: 0/Rock, 1/Paper, 2/Scissors...')
        sleep(2)
        action = input('Enter the action you want to play: ').strip().lower()
        if action == "0" or action == "rock":
            action = 0
            print('You: Rock')
            if computer == action:
                print('Computer: Rock')
                sleep(1)
                print('Draw!')
                scoreboard_user = scoreboard_user + 1
                scoreboard_computer = scoreboard_computer + 1
                print("=====Score======")
                print("You ", scoreboard_user, "X Computer ",
                      scoreboard_computer)
                sleep(2)
                os.system('clear')
                os.system('cls')
            elif computer == 1:
                print('Computer: Paper')
                sleep(1)
                print('Computer wins!')
                scoreboard_computer = scoreboard_computer + 1
                print("=====Score======")
                print("You ", scoreboard_user, "X Computer ",
                      scoreboard_computer)
                sleep(2)
                os.system('clear')
                os.system('cls')
            else:
                print('Computer: Scissors')
                sleep(1)
                print('You wins!')
                scoreboard_user = scoreboard_user + 1
                print("=====Score======")
                print("You ", scoreboard_user, "X Computer ",
                      scoreboard_computer)
                sleep(2)
                os.system('clear')
                os.system('cls')

        elif action == "1" or action == "paper":
            action = 1
            print('Paper')
            if computer == action:
                print('Computer: Paper')
                sleep(1)
                print('Draw!')
                scoreboard_user = scoreboard_user + 1
                scoreboard_computer = scoreboard_computer + 1
                print("=====Score======")
                print("User ", scoreboard_user, "X Computer ",
                      scoreboard_computer)
                sleep(2)
                os.system('clear')
                os.system('cls')
            elif computer == 2:
                print('Computer: Scissors')
                sleep(1)
                print('Computer wins!')
                scoreboard_computer = scoreboard_computer + 1
                print("=====Score======")
                print("User ", scoreboard_user, "X Computer ",
                      scoreboard_computer)
                sleep(2)
                os.system('clear')
                os.system('cls')
            else:
                print('Computer: Rock')
                sleep(1)
                print('You wins!')
                scoreboard_user = scoreboard_user + 1
                print("=====Score======")
                print("User ", scoreboard_user, "X Computer ",
                      scoreboard_computer)
                sleep(2)
                os.system('clear')
                os.system('cls')

        elif action == "2" or action == "scissors":
            action = 2
            print('Scissors')
            if computer == action:
                print('Computer: Scissors')
                sleep(1)
                print('Draw!')
                scoreboard_user = scoreboard_user + 1
                scoreboard_computer = scoreboard_computer + 1
                print("=====Score======")
                print("User ", scoreboard_user, "X Computer ",
                      scoreboard_computer)
                sleep(2)
                os.system('clear')
                os.system('cls')
            elif computer == 0:
                print('Computer: Rock')
                sleep(1)
                print('Computer wins')
                scoreboard_computer = scoreboard_computer + 1
                print("=====Score======")
                print("User ", scoreboard_user, "X Computer ",
                      scoreboard_computer)
                sleep(2)
                os.system('clear')
                os.system('cls')
            else:
                print('Computer: Paper')
                sleep(1)
                print('You wins!')
                scoreboard_user = scoreboard_user + 1
                print("=====Score======")
                print("User ", scoreboard_user, "X Computer ",
                      scoreboard_computer)
                sleep(2)
                os.system('clear')
                os.system('cls')
                choice = ("You want play yet?").strip().lower()
                if choice == "yes" or choice == "y" or choice == "1":
                    print("OK, let's to this!")
                elif choice == "no" or choice == "n" or choice == "0":
                    print("Ok, thanks for play!")
                    sys.exit()
                choice = ("You want play yet?").strip().lower()
                if choice == "yes" or choice == "y" or choice == "1":
                    print("OK, let's to this!")
                elif choice == "no" or choice == "n" or choice == "0":
                    print("Ok, thanks for play!")
                    sys.exit()

        else:
            print("Wrong action, try again!")
            os.system('clear')
            os.system('cls')
        print("You want play yet?")
        choice = input(
            "Answer with 1/Yes or 0/No to continue: ").strip().lower()
        if choice == "yes" or choice == "y" or choice == "1":
            print("OK, let's to this!")
            os.system('clear')
            os.system('cls')
        elif choice == "no" or choice == "n" or choice == "0":
            print("Ok, thanks for play!")
            sys.exit()
