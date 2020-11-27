import random

if __name__ == "__main__":
    options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    list_win = {"Rock": {"Lizard": "crushes", "Scissors": "crushes"},
                "Paper": {"Rock": "covers", "Spock": "disproves"},
                "Scissors": {"Paper": "cuts", "Lizard": "decapitates"},
                "Lizard": {"Paper": "eats", "Spock": "poison"},
                "Spock": {"Rock": "vaporizes", "Scissors": "smashes"}
                }

    computer = random.choice(options)

    player = False

    while not player:

        player = input("Rock, Paper, Scissors, Lizard, Spock ? : ")
        if player not in options:
            print("That's not a valid option.")
        elif player == computer:
            print("It's a Tie!".format())
        else:
            if computer in list_win[player]:
                order_player1 = player
                order_player2 = computer
                result = "Win"
            else:
                order_player1 = computer
                order_player2 = player
                result = "Lose"

            for key, value in list_win[order_player1].items():
                if key == order_player2:
                    print("You {}, {} {} {}".format(result, order_player1, value, order_player2))

        player = False
        computer = random.choice(options)
