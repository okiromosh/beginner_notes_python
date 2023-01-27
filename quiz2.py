def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num - 1]:
            # for every item in options, display index of question_num -1 ie 1-1 which will display index[0]
            print(i)

        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)  # collects all the input guess into the list guesses

        correct_guesses += check_answer(questions.get(key), guess)
        # (question_num + 1) = (2 -1) = 1, thus display options to index[1], then to index[2], then to index[3]
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0


def display_score(correct_guesses, guesses):
    print("-----------------")
    print("ANSWERS")
    print("-----------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score_num = int(correct_guesses)
    score = int((correct_guesses / len(questions)) * 100)
    print(f"You got {score_num} answers correct")
    print(f"Your score is {score}%")


def play_again():
    response = input("Would you like to try again? (y/n): ").lower()

    if response == "y":
        return True
    else:
        return False


questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tribute to which comedy group?: ": "C",
    "Is the earth round?: ": "A"
}
options = [
    ["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zukerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smooch", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What is earth"]
]

new_game()
while play_again():
    new_game()

print("Thank you!")
