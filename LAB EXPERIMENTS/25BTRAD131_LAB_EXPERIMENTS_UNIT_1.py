"""
JAIN (DEEMED-TO-BE UNIVERSITY) - FACULTY OF ENGINEERING & TECHNOLOGY (SET)
Department of Computer Science & Engineering (AI & DE)
Course / Lab: Python Programming Laboratory
Semester & Sec: 3rd Semester | Class: CSE-AIDE (B)
Academic Year: 2026 – 2027

LAB EXPERIMENTS – UNIT 1: Environment Configuration, Basic I/O, Operators & Computational Math
Student Name: Vishanth R
Register / USN: 25BTRAD131
"""

import math


def lab_exercise_1_setup_docs():
    """Lab Exercise 1: Installing Python, VS Code, and Environment Setup
    Comprehensive installation walkthrough, PATH environment configuration, and Visual Studio Code setup.
    """
    docs = """
================================================================================
Lab Exercise 1: Environment Configuration & Toolchain Setup
================================================================================
Section 1: Windows Setup & Verification
  Step 1: Download Python Installer via Chrome (python.org/downloads)
  Step 2: Run Installer & check 'Add python.exe to PATH' and 'Install for all users'
  Step 3: Verification via Command Prompt: python --version

Section 2: Setting up Visual Studio Code & Extensions
  1. Install VS Code from code.visualstudio.com
  2. Launch workspace from terminal: code .
  3. Install official Microsoft Python Extension
  4. Enable File -> Auto Save
  5. Open Project Workspace (Ctrl+K Ctrl+O) and create script files.
================================================================================
"""
    print(docs)


def lab_exercise_2_basic_program():
    """Lab Exercise 2: Write and Execute a Basic Python Program
    Verify Python interpreter execution with introductory print statements.
    """
    print("=== Lab Exercise 2: Basic Python Program ===")
    print("Hello, World!")
    print("Welcome to Python Programming.")
    print()


def lab_exercise_3_variables_io(name="Vishanth R", age=20):
    """Lab Exercise 3: Programs Using Variables, Operators, and Input/Output
    Interactive input acquisition, arithmetic operator execution, and formatted string interpolation.
    """
    print("=== Lab Exercise 3: Variables, Operators & I/O ===")
    # Basic Arithmetic Operators
    next_year_age = age + 1
    double_age = age * 2

    # Output using formatted string (f-string)
    print(f"Hello, {name}!")
    print(f"You are currently {age} years old.")
    print(f"Next year, you will be {next_year_age} years old.")
    print(f"Twice your age is {double_age}.")
    print()


def lab_exercise_4a_calculator(num1=25.0, num2=5.0):
    """Lab Exercise 4 - Part A: Simple Calculator (Arithmetic Operations)
    Implements basic arithmetic operations: addition, subtraction, multiplication, and safe division.
    """
    print("=== Lab Exercise 4 (Part A): Simple Calculator ===")
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

    print(f"Addition:       {num1} + {num2} = {addition}")
    print(f"Subtraction:    {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division:       {num1} / {num2} = {division}")
    print()


def lab_exercise_4b_area_calculations(length=12.0, width=8.0, radius=7.0):
    """Lab Exercise 4 - Part B: Area Calculation Programs (Geometric Formulas)
    Computes geometric surface area of rectangles and circles utilizing Python math constants.
    """
    print("=== Lab Exercise 4 (Part B): Area Calculations ===")
    # 1. Area of a Rectangle
    area_rectangle = length * width
    print(f"Rectangle (length={length}, width={width}) -> Area: {area_rectangle:.2f}")

    # 2. Area of a Circle
    area_circle = math.pi * (radius ** 2)
    print(f"Circle (radius={radius}) -> Area: {area_circle:.2f}")
    print()


def main():
    print("=" * 60)
    print("LAB EXPERIMENTS – UNIT 1: Basic I/O, Operators & Math")
    print("Developer: Vishanth R | Register: 25BTRAD131")
    print("=" * 60)
    print()
    lab_exercise_1_setup_docs()
    lab_exercise_2_basic_program()
    lab_exercise_3_variables_io()
    lab_exercise_4a_calculator()
    lab_exercise_4b_area_calculations()
    print("=" * 60)
    print("Unit 1 Lab Experiments executed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
