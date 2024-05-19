import random
options_list = ("rock", "paper", "scissors")
repeat = True
while repeat:
    player = None
    computer = random.choice(options_list)
    while player not in options_list:
        player = input("Enter your choice: ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    if input("Play again? (y/n): ").lower() != "y":
        repeat = False
print("Thanks for playing!")