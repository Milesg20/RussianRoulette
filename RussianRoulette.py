import random

def RussianRoulette():
    chambers_left = 6
    players = ["Player", "Opponent"]
    turn = 0

    print("Welcome to Russian Roulette. Try to survive!")

    while chambers_left > 0:
        current_player = players[turn % 2]

        print(f"\n{current_player}'s turn:")

        if current_player == "Player":
            choice = input("Pull trigger? (y/n) ").lower()
            if choice != 'y':
                print("You chickened out! Game over.")
                return
        else:
            print("Opponent pulls the trigger...")

        chamber = random.randint(1, chambers_left)

        if chamber == 1:
            print(f"BANG! {current_player} died.")
            print(f"{players[(turn+1)%2]} wins!")
            return
        else:
            chambers_left -= 1
            print(f"*click* {current_player} survived. {chambers_left} chambers left.")

        turn += 1

    print("\nAll chambers empty. It's a draw!")

# Runs the game
RussianRoulette()
