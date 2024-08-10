import random


def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"


def play_game():
    user_wins = 0
    com_win = 0

    while True:
        user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
        if user_input == 'q':
            break

        if user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose Rock, Paper, or Scissors.")
            continue

        computer_pick = get_computer_choice()
        print(f'Computer pick: {computer_pick}.')

        result = determine_winner(user_input, computer_pick)
        if result == "user":
            print("You win!!")
            user_wins += 1
        elif result == "computer":
            print("You lose!!")
            com_win += 1
        else:
            print("Draw!!")

    print(f"\nYou won {user_wins} times.")
    print(f"Computer won {com_win} times.")
    print("Goodbye!!")


if __name__ == '__main__':
    play_game()
