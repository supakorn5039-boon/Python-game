import random


def get_user_input(prompt, validate_func):
    while True:
        user_input = input(prompt)
        if validate_func(user_input):
            return user_input
        print("Invalid input. Please try again.")


def is_positive_integer(value):
    return value.isdigit() and int(value) > 0


def get_valid_number(prompt):
    return int(get_user_input(prompt, is_positive_integer))


def main():
    top_of_range = get_valid_number("Enter a number greater than 0: ")

    random_num = random.randint(1, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = get_valid_number("Make a guess: ")

        if user_guess == random_num:
            print(f'You got it in {guesses} tries!')
            break
        elif user_guess > random_num:
            print("Too high!")
        else:
            print("Too low!")


if __name__ == "__main__":
    main()
