import random,numbers


def guess_number():
    randNum = random.randint(1, 9)
    guess = False

    while not guess:
        userInput = input("Enter a Number : ")
        if userInput == "":
            print("Please input a number")
        else:
            userInput = int(userInput)
            if userInput == randNum:
                print("Exactly Right")
                guess = True
            elif userInput > randNum:
                print("Too High")
            else:
                print("Too Low")


if __name__ == "__main__":
    print(guess_number())
