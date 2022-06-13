import time
import random


def intro(enemy):
    printPause("You find yourself standing in an open field,"
               " filled with grass and yellow wildflowers.")
    printPause(f"Rumor has it that a wicked {enemy}, is somewhere around "
               "here, and has been terrifying the nearby village.\n")


def printPause(printString):
    print(printString)
    time.sleep(1)


def action(items, enemy):
    printPause("Enter 1 to knock on the door of the house.")
    printPause("Enter 2 to peer into the cave.")
    printPause("What would you like to do?")
    while True:
        roomChoice = input("(Please enter 1 or 2).\n")
        if roomChoice == '1':
            house(items, enemy)
            break
        elif roomChoice == '2':
            cave(items, enemy)
            break


def cave(items, enemy):
    if "sword" in items:
        printPause("You peer cautiously into the cave.")
        printPause("You have already been here and the cave is empty now.")
        printPause("You walk back to the field.\n")
        action(items, enemy)
    elif "dagger" in items:
        printPause("You peer cautiously into the cave.")
        printPause("It turns out to be a small cave.")
        printPause("Your eye catches a glint of metal behind a rock.")
        printPause("You have found the magical sword of Vaughn.")
        printPause("Your discard the silly dagger for the sword.")
        printPause("You walk back to the field.\n")
        items.append("sword")
        action(items, enemy)


def house(items, enemy):
    printPause("You approach the door of the house.")
    printPause(f"You are about to knock when the door opens"
               f" and out steps a {enemy}")
    printPause(f"Yikes! This is the {enemy}'s house.")
    printPause(f"The {enemy} attacks you.")
    if "sword" not in items:
        printPause("You feel underprepared with only a dagger.")
    while True:
        fightChoice = input("Would you like to (1) fight or (2) run away?\n")
        if fightChoice == '1':
            if "sword" in items:
                victory(enemy)
            else:
                defeat(enemy)
            break
        elif fightChoice == '2':
            runAway(items, enemy)
            break


def victory(enemy):
    printPause("The sword shines brightly in your hand as "
               "you brace for combat.")
    printPause(f"But the {enemy} takes one look at the sword and runs away!")
    printPause(f"You have rid the town of the {enemy}. You are victorious!")
    playAgain()


def defeat(enemy):
    printPause("You do your best...")
    printPause(f"But your dagger is no match for the {enemy}.")
    printPause("You have been defeated!")
    playAgain()


def runAway(items, enemy):
    printPause("You run back to the field. Luckily, "
               "you dont seem to have been followed.")
    action(items, enemy)


def playAgain():
    while True:
        playAgainChoice = input("Would you like to play again? (y/n)\n")
        if playAgainChoice == 'y':
            playGame()
            break
        elif playAgainChoice == 'n':
            exit()


def playGame():
    items = []
    enemy = random.choice(["troll", "fairy", "pirate", "dragon"])
    items.append("dagger")
    intro(enemy)
    action(items, enemy)


playGame()
