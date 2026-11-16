"""
JAIN (DEEMED-TO-BE UNIVERSITY) - FACULTY OF ENGINEERING & TECHNOLOGY (SET)
Department of Computer Science & Engineering (AI & DE)
Course / Lab: Python Programming Laboratory
Semester & Sec: 3rd Semester | Class: CSE-AIDE (B)
Academic Year: 2026 – 2027

LAB EXPERIMENTS – UNIT 2: Control Structures, Modular Functions, Loop Logics & Recursion
Student Name: Vishanth R
Register / USN: 25BTRAD131
"""

import math
import random


def number_guessing_game(simulated_guesses=None):
    """Lab Exercise 5: Number Guessing Game (Loops & Random Module)
    Implement an interactive number guessing game using random generation, while loops, and branch comparisons.
    Supports simulated_guesses list for non-interactive automated testing.
    """
    print("=== Lab Exercise 5: Number Guessing Game ===")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    guess_iter = iter(simulated_guesses) if simulated_guesses is not None else None

    while not guessed_correctly:
        try:
            if guess_iter is not None:
                try:
                    user_guess = next(guess_iter)
                    print(f"Testing Guess: {user_guess}")
                except StopIteration:
                    print(f"[Simulated run finished. Secret was: {number_to_guess}]")
                    break
            else:
                user_guess = int(input("Enter your guess: "))

            attempts += 1
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    print()


def is_prime(n):
    """Evaluates whether an integer n is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_factorial(n):
    """Computes factorial of non-negative integer n with edge case handling."""
    if n < 0:
        return "Undefined (factorial does not exist for negative numbers)"
    return math.factorial(n)


def lab_exercise_6_prime_and_factorial(test_numbers=(7, 12, 0, -5)):
    """Lab Exercise 6: Prime Number and Factorial Programs
    Modular program to evaluate prime status of a number and compute factorial with robust edge case handling.
    """
    print("=== Lab Exercise 6: Prime Number and Factorial Program ===")
    for number in test_numbers:
        prime_status = "a PRIME number" if is_prime(number) else "NOT a prime number"
        fact = get_factorial(number)
        print(f"Number: {number:>3} | Prime Status: {prime_status:<18} | Factorial: {fact}")
    print()


def fibonacci_recursive(n):
    """Recursive Fibonacci term calculation."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def lab_exercise_7_fibonacci(n_terms=10):
    """Lab Exercise 7: Fibonacci Series Using Recursion
    Implement a recursive Fibonacci algorithm to compute terms and display comma-separated sequences.
    """
    print("=== Lab Exercise 7: Fibonacci Series Using Recursion ===")
    if n_terms <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        fib_series = [str(fibonacci_recursive(i)) for i in range(n_terms)]
        print(f"Fibonacci Series ({n_terms} terms):")
        print(", ".join(fib_series))
    print()


def main():
    print("=" * 60)
    print("LAB EXPERIMENTS – UNIT 2: Control Structures & Recursion")
    print("Developer: Vishanth R | Register: 25BTRAD131")
    print("=" * 60)
    print()
    # Demonstration runs
    random.seed(42)
    number_guessing_game(simulated_guesses=[50, 75, 88, 94])
    lab_exercise_6_prime_and_factorial()
    lab_exercise_7_fibonacci(10)
    print("=" * 60)
    print("Unit 2 Lab Experiments executed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
