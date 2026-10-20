

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "define", "fun"],
        "answer": "B"
    },
    {
        "question": "Which data type stores multiple key-value pairs in Python?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "$"],
        "answer": "B"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["input()", "display()", "print()", "output()"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["String", "Integer", "Boolean", "List"],
        "answer": "C"
    }
]


def show_instructions():
    print("\n===== QUIZ INSTRUCTIONS =====")
    print("1. The quiz contains 5 questions.")
    print("2. Each question has four options: A, B, C, D.")
    print("3. Enter the letter of your chosen answer.")
    print("4. Each correct answer earns one point.")
    print("5. Incorrect answers receive zero points.")
    print("6. Your final score will be displayed at the end.")


def start_quiz():
    correct = 0
    incorrect = 0
    total = len(questions)

    print("\n===== WELCOME TO THE QUIZ =====")
    print("Answer all the questions!\n")

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for j, option in enumerate(q["options"]):
            print(f"{chr(65 + j)}. {option}")

        while True:
            try:
                answer = input("Enter your answer (A/B/C/D): ").strip().upper()

                if answer in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid choice! Please enter A, B, C, or D.")

            except (EOFError, KeyboardInterrupt):
                print("\nQuiz interrupted.")
                return

        if answer == q["answer"]:
            print("Correct answer!")
            correct += 1
        else:
            correct_answer = q["answer"]
            correct_option = q["options"][ord(correct_answer) - 65]
            print(f"Incorrect! Correct answer: {correct_answer}. {correct_option}")
            incorrect += 1

    percentage = (correct / total) * 100

    print("\n===== QUIZ RESULTS =====")
    print("Total Questions:", total)
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print(f"Final Score: {percentage:.2f}%")

    if percentage == 100:
        print("Performance: Excellent!")
    elif percentage >= 70:
        print("Performance: Good job!")
    elif percentage >= 40:
        print("Performance: Keep practicing!")
    else:
        print("Performance: Don't give up! Try again.")


def main():
    while True:
        print("\n===== QUIZ APPLICATION =====")
        print("1. Start Quiz")
        print("2. View Quiz Instructions")
        print("3. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                start_quiz()

                while True:
                    replay = input(
                        "\nWould you like to play again? (yes/no): "
                    ).strip().lower()

                    if replay in ["yes", "y"]:
                        break
                    elif replay in ["no", "n"]:
                        print("Returning to the main menu...")
                        break
                    else:
                        print("Please enter yes or no.")

                if replay in ["yes", "y"]:
                    continue

            elif choice == "2":
                show_instructions()

            elif choice == "3":
                print("Thank you for using the Quiz Application!")
                break

            else:
                print("Invalid menu choice! Please select 1, 2, or 3.")

        except (EOFError, KeyboardInterrupt):
            print("\nExiting Quiz Application. Goodbye!")
            break


if __name__ == "__main__":
    main()
