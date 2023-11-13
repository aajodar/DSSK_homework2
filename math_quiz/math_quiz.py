import random


def rand_int(min:int, max:int) -> int:
    """
    Generate a random integer within the specified range.
    """
    return random.randint(min, max)


def rand_operation() -> str:
    """
    Generate a random arithmetic operator: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def do_operation(n1: int, n2: int, operator: str) -> tuple:
    """
    Perform the arithmetic operation based on the given numbers and operator.
    Returns a tuple containing the problem and the correct answer.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    return problem, answer


def math_quiz() -> None:
    """
    Conduct a math quiz game, asking the user to solve arithmetic problems.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = rand_int(1, 10)
        num2 = rand_int(1, 5)
        operator = rand_operation()

        problem, correct_answer = do_operation(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
