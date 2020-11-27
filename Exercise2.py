import random


def guessNumber():
    randNum = random.randint(0, 9)
    guess = False

    while not guess:
        userInput = int(input("Enter a Number"))
        if userInput == randNum:
            print("Exactly Right")
            guess = True
        elif userInput > randNum:
            print("Too High")
        else:
            print("Too Low")
