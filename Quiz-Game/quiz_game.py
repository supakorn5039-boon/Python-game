def play_quiz():
    print("Welcome to my computer quiz!")

    if input("Do you want to play? ").strip().lower() != "yes":
        quit()

    print("Okay! Let's play :)")
    score = 0

    questions = {
        "What does CPU stand for? ": "central processing unit",
        "What does GPU stand for? ": "graphics processing unit",
        "What does RAM stand for? ": "random access memory",
        "What does PSU stand for? ": "power supply"
    }

    for question, correct_answer in questions.items():
        answer = input(question).strip().lower()
        if answer == correct_answer:
            print("Correct")
            score += 1
        else:
            print("Incorrect")

    print(f"You got {score} questions correct!")
    print(f"Your score is {(score / len(questions)) * 100}%")


# Call the function to play the quiz
if __name__ == "__main__":
    play_quiz()
