"""
JAIN (DEEMED-TO-BE UNIVERSITY) - FACULTY OF ENGINEERING & TECHNOLOGY (SET)
Department of Computer Science & Engineering (AI & DE)
Course / Lab: Python Programming Laboratory
Semester & Sec: 3rd Semester | Class: CSE-AIDE (B)
Academic Year: 2026 – 2027

ASSIGNMENT TASK – PART 1: Python Programming Basics (Core Syntax, Pattern Loops & Variables)
Student Name: Vishanth R
Register / USN: 25BTRAD131
"""


def task_1_basic_console_output():
    """Task 1: Basic Console Output
    Print Name, Department, and College each on a separate line.
    """
    print("=== Task 1: Basic Console Output ===")
    print("Vishanth R")
    print("Computer Science & Engineering (AI & DE)")
    print("Jain (Deemed-to-be University)")
    print()


def task_2_nested_loops_pattern():
    """Task 2: Nested Loops Pattern Generation
    Print the pattern of stars (*) using nested for loops (3 rows x 7 cols).
    """
    print("=== Task 2: Nested Loops Pattern Generation ===")
    for i in range(3):
        for j in range(7):
            print("*", end="")
        print()
    print()


def task_3_single_statement_display():
    """Task 3: Single Statement String Display
    Print 'Python is Easy' using a single print() statement.
    """
    print("=== Task 3: Single Statement String Display ===")
    print("Python is Easy")
    print()


def task_4_number_pyramid():
    """Task 4: Number Pyramid Pattern
    Print the number pyramid pattern (1 to 12345) using loops.
    """
    print("=== Task 4: Number Pyramid Pattern ===")
    pattern = ""
    for i in range(1, 6):
        pattern += str(i)
        print(pattern)
    print()


def task_5_escape_sequence_newline():
    """Task 5: Escape Sequence \\n (Newlines)
    Use \\n to print Computer, Science, and Engineering on separate lines using a single print statement.
    """
    print("=== Task 5: Escape Sequence \\n (Newlines) ===")
    print("Computer\nScience\nEngineering")
    print()


def task_6_escape_sequence_tab():
    """Task 6: Escape Sequence \\t (Horizontal Tabs)
    Use \\t to print tab-separated column headers: Name, Age, City.
    """
    print("=== Task 6: Escape Sequence \\t (Horizontal Tabs) ===")
    print("Name\tAge\tCity")
    print()


def task_7_single_line_comments():
    """Task 7: Single-line Comments in Code
    Write a Python program with a single-line comment explaining its purpose.
    """
    print("=== Task 7: Single-line Comments in Code ===")
    # Program to calculate the area of a rectangle
    length = 5
    width = 10
    print("Area:", length * width)
    print()


def task_8_multiline_comments():
    """Task 8: Multi-line Comments (Docstrings)
    Write a Python program with a multi-line comment enclosed in triple quotes.
    """
    print("=== Task 8: Multi-line Comments (Docstrings) ===")
    """
    Multi-line Comment
    This program calculates the simple interest.
    Formula: (P * R * T) / 100
    """
    principal = 1000
    rate = 5
    time = 2
    simple_interest = (principal * rate * time) / 100
    print("Simple Interest:", simple_interest)
    print()


def task_9_code_documentation():
    """Task 9: Code Documentation & Comments
    Write a program containing three comments and three print statements.
    """
    print("=== Task 9: Code Documentation & Comments ===")
    # Comment 1: Display greeting
    print("Hello!")
    # Comment 2: Display status
    print("Learning Python basics.")
    # Comment 3: Display farewell
    print("Goodbye!")
    print()


def task_10_variable_declaration():
    """Task 10: Variable Declaration & Output
    Create a variable called name, store your name in it, and print it.
    """
    print("=== Task 10: Variable Declaration & Output ===")
    name = "Vishanth R"
    print(name)
    print()


def task_11_multivariable_storage():
    """Task 11: Multi-Variable Storage & Output
    Store first name, last name, and age in variables. Print each variable on a separate line.
    """
    print("=== Task 11: Multi-Variable Storage & Output ===")
    first_name = "Vishanth"
    last_name = "R"
    age = 20
    print(first_name)
    print(last_name)
    print(age)
    print()


def main():
    print("=" * 60)
    print("ASSIGNMENT TASK - PART 1: Python Programming Basics")
    print("Developer: Vishanth R | Register: 25BTRAD131")
    print("=" * 60)
    print()
    task_1_basic_console_output()
    task_2_nested_loops_pattern()
    task_3_single_statement_display()
    task_4_number_pyramid()
    task_5_escape_sequence_newline()
    task_6_escape_sequence_tab()
    task_7_single_line_comments()
    task_8_multiline_comments()
    task_9_code_documentation()
    task_10_variable_declaration()
    task_11_multivariable_storage()
    print("=" * 60)
    print("All tasks completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
