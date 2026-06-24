import random

def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    """Return the result of the round."""
    if player == computer:
        return 'tie'
    winning_combos = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    if winning_combos[player] == computer:
        return 'player'
    return 'computer'

def get_player_choice():
    """Prompt the player for a valid choice."""
    shortcuts = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    while True:
        choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").strip().lower()
        if choice in shortcuts:
            return shortcuts[choice]
        if choice in shortcuts.values():
            return choice
        print("Invalid choice. Please enter r, p, or s.")

def main():
    print("=== Rock, Paper, Scissors ===\n")
    player_score = 0
    computer_score = 0

    while True:
        player = get_player_choice()
        computer = get_computer_choice()

        print(f"\nYou chose {player.capitalize()}, the computer chose {computer.capitalize()}.")

        result = determine_winner(player, computer)

        if result == 'tie':
            print(f"Both players selected {player.capitalize()}. It's a tie!")
        elif result == 'player':
            print(f"{player.capitalize()} beats {computer.capitalize()}! You win this round.")
            player_score += 1
        else:
            descriptions = {
                ('rock', 'paper'): 'Paper covers Rock!',
                ('scissors', 'rock'): 'Rock smashes Scissors!',
                ('paper', 'scissors'): 'Scissors cut Paper!'
            }
            msg = descriptions.get((player, computer), f"{computer.capitalize()} beats {player.capitalize()}!")
            print(f"{msg} You lose.")
            computer_score += 1

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

    print(f"\nFinal Scores:")
    print(f"Computer: {computer_score}")
    print(f"Player: {player_score}")

if __name__ == "__main__":
    main()
