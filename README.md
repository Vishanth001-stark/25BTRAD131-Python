# 25BTRAD131 - Python Programming Laboratory

This repository contains academic coursework source code, laboratory experiment implementations, mini-projects, and experiential learning programs for the **Python Programming Laboratory** course.

---

## 👤 Student Profile

- **Name:** Vishanth R
- **Register / USN:** 25BTRAD131
- **Program / Branch:** B.Tech – Computer Science & Engineering (AI & Data Engineering)
- **Course / Lab:** Python Programming Laboratory (25CSE204)
- **Institution:** Faculty of Engineering & Technology (SET), Jain (Deemed-to-be University)
- **Academic Year:** 2026 – 2027

---

## 📁 Repository Structure

```text
25BTRAD131-Python/
├── LAB EXPERIMENTS/
│   ├── 25BTRAD131_ASSIGNMENT_TASK_PART_1.py
│   ├── 25BTRAD131_LAB_EXPERIMENTS_UNIT_1.py
│   ├── 25BTRAD131_LAB_EXPERIMENTS_UNIT_2.py
│   ├── 25BTRAD131_LAB_EXPERIMENTS_UNIT_3.py
│   ├── 25BTRAD131_LAB_EXPERIMENTS_UNIT_4.py
│   └── 25BTRAD131_LAB_EXPERIMENTS_UNIT_5.py
│
├── MINI PROJECT/
│   ├── 25BTRAD131_MINI_PROJECT_UNIT_1.py
│   ├── 25BTRAD131_MINI_PROJECT_UNIT_2.py
│   └── 25BTRAD131_MINI_PROJECT_UNIT_3.py
│
└── Experiential Learning/
    ├── main.py
    ├── password_manager.py
    └── test_password_manager.py
```

---

## 📌 Contents Breakdown

### 1. LAB EXPERIMENTS

Each unit contains complete, runnable Python implementations with modular functions:

- **`25BTRAD131_ASSIGNMENT_TASK_PART_1.py`**:
  - Task 1: Basic Console Output
  - Task 2: Nested Loops Pattern Generation
  - Task 3: Single Statement String Display
  - Task 4: Number Pyramid Pattern
  - Task 5: Escape Sequence `\n` (Newlines)
  - Task 6: Escape Sequence `\t` (Horizontal Tabs)
  - Task 7: Single-line Comments in Code
  - Task 8: Multi-line Comments (Docstrings)
  - Task 9: Code Documentation & Comments
  - Task 10: Variable Declaration & Output
  - Task 11: Multi-Variable Storage & Output

- **`25BTRAD131_LAB_EXPERIMENTS_UNIT_1.py`**:
  - Exercise 1: Environment Configuration & Toolchain Setup Documentation
  - Exercise 2: Basic Python Program Execution
  - Exercise 3: Variables, Operators & Formatted Input/Output
  - Exercise 4 (Part A): Simple Calculator (Arithmetic Operations)
  - Exercise 4 (Part B): Geometric Area Calculations (Rectangle & Circle)

- **`25BTRAD131_LAB_EXPERIMENTS_UNIT_2.py`**:
  - Exercise 5: Number Guessing Game (Random Generation & While Loops)
  - Exercise 6: Prime Number and Factorial Programs (Edge Case Validation)
  - Exercise 7: Fibonacci Series Using Recursion

- **`25BTRAD131_LAB_EXPERIMENTS_UNIT_3.py`**:
  - Exercise 8: Contact Book Using Lists & Dictionaries (CRUD Operations)
  - Exercise 9: Student Academic Grading System (Boundary Analysis)
  - Exercise 10: Word & Element Frequency Counter Using Dictionaries

- **`25BTRAD131_LAB_EXPERIMENTS_UNIT_4.py`**:
  - Exercise 11: Production Server Log File Analyzer & Keyword Summarizer
  - Exercise 12: Student Data Manager with Persistent File I/O (CRUD)
  - Exercise 13: CSV-Based Enterprise Payroll Management System

- **`25BTRAD131_LAB_EXPERIMENTS_UNIT_5.py`**:
  - Exercise 14: Bank Account Management System (OOP, Encapsulation & Validation)
  - Exercise 15: Central Library Management System (OOP & Inheritance)
  - Exercise 16: Multi-Dice Monte Carlo Simulation & Outcome Frequency Analysis

---

### 2. MINI PROJECT

Comprehensive project solutions integrating GUI development, cryptography, and data analytics:

- **`25BTRAD131_MINI_PROJECT_UNIT_1.py`**:
  - Multi-Category Unit Converter (Length, Weight, Temperature).
  - Built with Tkinter GUI and includes headless `--cli` mode.
- **`25BTRAD131_MINI_PROJECT_UNIT_2.py`**:
  - Secure OTP Generator & Verification System.
  - Supports numeric & alphanumeric tokens, SHA-256 digest auditing, phone number masking, and 60-second time-to-live verification.
- **`25BTRAD131_MINI_PROJECT_UNIT_3.py`**:
  - Problem 1: Classroom Attendance Tracker (Nested Dictionaries, Session Logging, Attendance Shortage Audit).
  - Problem 2: Retail Sales Data Analyzer (Inventory Management, Revenue Computation, Multi-Dataset Comparison).

---

### 3. Experiential Learning (ExpLe)

Production-grade secure password storage vault:
- **`password_manager.py`**: Core cryptographic engine with PBKDF2 hashing, AES/Fernet encryption, and persistent pickle storage.
- **`main.py`**: Interactive CLI vault interface with masked master password authentication.
- **`test_password_manager.py`**: Complete unit test suite verifying vault integrity and cryptographic operations.

---

## 🚀 How to Run

Execute any script directly using Python 3:

```bash
# Run Lab Experiments
python "LAB EXPERIMENTS/25BTRAD131_ASSIGNMENT_TASK_PART_1.py"
python "LAB EXPERIMENTS/25BTRAD131_LAB_EXPERIMENTS_UNIT_1.py"
python "LAB EXPERIMENTS/25BTRAD131_LAB_EXPERIMENTS_UNIT_2.py"
python "LAB EXPERIMENTS/25BTRAD131_LAB_EXPERIMENTS_UNIT_3.py"
python "LAB EXPERIMENTS/25BTRAD131_LAB_EXPERIMENTS_UNIT_4.py"
python "LAB EXPERIMENTS/25BTRAD131_LAB_EXPERIMENTS_UNIT_5.py"

# Run Mini Projects
python "MINI PROJECT/25BTRAD131_MINI_PROJECT_UNIT_1.py"        # GUI mode
python "MINI PROJECT/25BTRAD131_MINI_PROJECT_UNIT_1.py" --cli  # Headless CLI mode
python "MINI PROJECT/25BTRAD131_MINI_PROJECT_UNIT_2.py" --test # Test mode
python "MINI PROJECT/25BTRAD131_MINI_PROJECT_UNIT_3.py"

# Run Experiential Learning Tests
python "Experiential Learning/test_password_manager.py"
```
