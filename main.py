import random

choices = ["stone", "paper", "scissor"]
def get_choice():

    while True:

        user = input("Enter your choice (stone/paper/scissor): ").lower()

        if user in choices:
            return user

        elif user == "exit":
            return "exit"

        else:
            print("Invalid input! Try again.")
def check_winner(user, opponent):

    if user == opponent:
        return "draw"

    elif (
        (user == "stone" and opponent == "scissor") or
        (user == "paper" and opponent == "stone") or
        (user == "scissor" and opponent == "paper")
    ):
        return "user"

    else:
        return "opponent"


print("=" * 60)
print("        ROCK PAPER SCISSOR GAME")
print("=" * 60)

n = int(input("Enter number of rounds: "))

player = input("Play with (friend/computer): ").lower()

user_score = 0
computer_score = 0
friend_score = 0
for i in range(n):

    print(f"\n========== ROUND {i+1} ==========")
    if player == "computer":

        user = get_choice()

        if user == "exit":
            print("Game exited.")
            break

        computer = random.choice(choices)

        print(f"\nYou chose      : {user}")
        print(f"Computer chose : {computer}")

        result = check_winner(user, computer)

        if result == "draw":
            print("\nIt's a Draw!")

        elif result == "user":
            print("\nYou Win This Round!")
            user_score += 1

        else:
            print("\nComputer Wins This Round!")
            computer_score += 1

        print(f"\nYour Score     : {user_score}")
        print(f"Computer Score : {computer_score}")

    
    elif player == "friend":

        print("\nPlayer 1 Turn")
        user1 = get_choice()

        if user1 == "exit":
            print("Game exited.")
            break

        print("\nPlayer 2 Turn")
        user2 = get_choice()

        if user2 == "exit":
            print("Game exited.")
            break

        print(f"\nPlayer 1 chose : {user1}")
        print(f"Player 2 chose : {user2}")

        result = check_winner(user1, user2)

        if result == "draw":
            print("\nIt's a Draw!")

        elif result == "user":
            print("\nPlayer 1 Wins This Round!")
            user_score += 1

        else:
            print("\nPlayer 2 Wins This Round!")
            friend_score += 1

        print(f"\nPlayer 1 Score : {user_score}")
        print(f"Player 2 Score : {friend_score}")

    else:
        print("Invalid game mode!")
        break


print("\n" + "=" * 60)
print("              FINAL RESULT")
print("=" * 60)

if player == "computer":

    print(f"Your Final Score     : {user_score}")
    print(f"Computer Final Score : {computer_score}")

    if user_score == computer_score:
        print("\nMatch Draw!")

    elif user_score > computer_score:
        print("\nCongratulations! You Won The Game!")

    else:
        print("\nBetter Luck Next Time!")

elif player == "friend":

    print(f"Player 1 Final Score : {user_score}")
    print(f"Player 2 Final Score : {friend_score}")

    if user_score == friend_score:
        print("\nMatch Draw!")

    elif user_score > friend_score:
        print("\nPlayer 1 Wins The Game!")

    else:
        print("\nPlayer 2 Wins The Game!"  )