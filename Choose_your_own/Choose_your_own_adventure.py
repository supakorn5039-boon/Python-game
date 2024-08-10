def get_input(prompt):
    return input(prompt).strip().lower()


def adventure_game():
    name = get_input("Type your name: ").capitalize()
    print(f"Welcome {name} to this adventure!")

    answer = get_input("You are on a dirt road, it has come to an end and you can go left or right."
                       "\nWhich way would you like to go?\nAnswer: ")

    if answer == "left":
        answer = get_input("You come to a river, you can walk around it or swim across?\n"
                           "Type 'walk' to walk around or 'swim' to swim across?\nAnswer: ")
        if answer == "swim":
            print("You swim across and were eaten by an alligator.")
        elif answer == 'walk':
            print("You walked for many miles, ran out of water and you lost the game!!")
        else:
            print("Not a valid option. You lose!")

    elif answer == 'right':
        answer = get_input("You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)?"
                           "\nAnswer: ")
        if answer == 'back':
            print("You go back and lose!!")
        elif answer == 'cross':
            answer = get_input("You crossed the bridge and meet a stranger. Do you talk to them (yes/no)?\nAnswer: ")

            if answer == "yes":
                print("You talk to the stranger and they give you gold.\nYou WIN!!!!")
            elif answer == "no":
                print("You ignore the stranger and they are offended. You lose!!")
            else:
                print("Not a valid option. You lose!")
        else:
            print("Not a valid option. You lose!")

    else:
        print("That's not a valid option. You lose!")

    print(f"Thank you for trying, {name}!")


if __name__ == '__main__':
    adventure_game()
