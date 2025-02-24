import random

def get_computer_choice():
    """Generates a random choice for the computer (rock, paper, or scissors)."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    """Gets the player's choice through input and validates it."""
    while True:
        player_input = input("Choose rock, paper, or scissors: ").lower()
        if player_input in ["rock", "paper", "scissors"]:
            return player_input
        else:
            print("Invalid choice. Please choose between rock, paper, or scissors.")

def determine_winner(player_choice, computer_choice):
    """Determines the winner of the round based on player and computer choices."""
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_round():
    """Plays a single round of Rock Paper Scissors."""
    computer_choice = get_computer_choice()
    player_choice = get_player_choice()
    result = determine_winner(player_choice, computer_choice)
    print(result)
    return result  # Return the result for score keeping if needed

def play_game():
    """Plays the Rock Paper Scissors game in multiple rounds."""
    player_score = 0
    computer_score = 0
    round_number = 1

    print("Welcome to Rock Paper Scissors!")

    while True:
        print(f"\n----- Round {round_number} -----")
        round_result = play_round()

        if round_result == "You win!":
            player_score += 1
        elif round_result == "Computer wins!":
            computer_score += 1

        print(f"\nScore: You - {player_score}, Computer - {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break  # Exit the loop if player doesn't want to play again
        round_number += 1

    print("\nGame Over!")
    print(f"Final Score: You - {player_score}, Computer - {computer_score}")
    if player_score > computer_score:
        print("Congratulations! Early out ka!")
    elif computer_score > player_score:
        print("Dahil talo ka, OT ka + Lakad pauwi!")
    else:
        print("Tie")

# Start the game
if __name__ == "__main__":
    play_game()
