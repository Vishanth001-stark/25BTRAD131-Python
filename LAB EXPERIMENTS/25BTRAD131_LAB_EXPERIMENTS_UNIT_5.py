"""
JAIN (DEEMED-TO-BE UNIVERSITY) - FACULTY OF ENGINEERING & TECHNOLOGY (SET)
Department of Computer Science & Engineering (AI & DE)
Course / Lab: Python Programming Laboratory
Semester & Sec: 3rd Semester | Class: CSE-AIDE (B)
Academic Year: 2026 – 2027

LAB EXPERIMENTS – UNIT 5: Object-Oriented Programming (OOP) & Random Simulation
Student Name: Vishanth R
Register / USN: 25BTRAD131
"""

import random


# ==============================================================================
# Lab Exercise 14: Bank Account System Using OOP (Encapsulation & Validation)
# ==============================================================================
class BankAccount:
    """Base class encapsulating account balance, details, and transaction history."""

    def __init__(self, acc_no, holder, balance=0.0):
        self.__acc_no = acc_no
        self.__holder = holder
        self.__balance = float(balance)
        self.__ledger = [("INITIAL", balance, self.__balance)]

    def deposit(self, amount):
        if amount <= 0:
            print(f"[REJECTED] Deposit failed: Rs.{amount:.2f} must be positive.")
            return False
        self.__balance += amount
        self.__ledger.append(("DEPOSIT", amount, self.__balance))
        print(f"[SUCCESS] Deposited Rs.{amount:,.2f} | Balance: Rs.{self.__balance:,.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print(f"[REJECTED] Withdrawal failed: Rs.{amount:.2f} must be positive.")
            return False
        if amount > self.__balance:
            print(f"[DENIED] Insufficient funds! Req: Rs.{amount:,.2f}, Avail: Rs.{self.__balance:,.2f}")
            return False
        self.__balance -= amount
        self.__ledger.append(("WITHDRAW", amount, self.__balance))
        print(f"[SUCCESS] Withdrew Rs.{amount:,.2f} | Balance: Rs.{self.__balance:,.2f}")
        return True

    def display_statement(self):
        print("-" * 58)
        print(f"STATEMENT FOR {self.__acc_no} ({self.__holder})")
        print("-" * 58)
        print(f"{'TXN TYPE':<12} {'AMOUNT (Rs.)':<16} {'BALANCE (Rs.)':<16}")
        print("-" * 58)
        for txn, amt, bal in self.__ledger:
            print(f"{txn:<12} {amt:<16,.2f} {bal:<16,.2f}")
        print("-" * 58)
        print(f"Closing Available Balance: Rs.{self.__balance:,.2f}")
        print()


def demo_bank_account():
    print("=== Lab Exercise 14: Bank Account System (OOP) ===")
    account = BankAccount("SB-2026-131", "Vishanth R", balance=10000.0)
    account.deposit(5000.0)      # Valid deposit
    account.withdraw(3500.0)     # Valid withdrawal
    account.deposit(-500.0)      # Invalid transaction test (rejected)
    account.withdraw(15000.0)    # Overdraft transaction test (insufficient funds)
    account.display_statement()  # Formatted transaction ledger


# ==============================================================================
# Lab Exercise 15: Library Management System Using OOP & Inheritance
# ==============================================================================
class MediaItem:
    """Base class modeling library assets with ID, title, author and availability."""

    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.is_available = True
        self.borrower = None

    def __str__(self):
        status = "Available" if self.is_available else f"Issued to {self.borrower}"
        return f"[{self.item_id}] {self.title:<24} | {self.author:<18} | {status}"


class Book(MediaItem):
    """Derived class inheriting MediaItem and adding publication edition."""

    def __init__(self, item_id, title, author, edition="Standard"):
        super().__init__(item_id, title, author)
        self.edition = edition


class Library:
    """Class managing book catalog, issue/return circulation, and auditing."""

    def __init__(self, name):
        self.name = name
        self.catalog = {}

    def add_book(self, book):
        self.catalog[book.item_id] = book

    def display_catalog(self):
        print("-" * 62)
        print(f"{self.name.upper()} - BOOK CATALOG")
        print("-" * 62)
        for b in self.catalog.values():
            print(b)
        print("-" * 62)

    def issue_book(self, book_id, member):
        book = self.catalog.get(book_id)
        if not book:
            print(f"[ERROR] Book ID '{book_id}' not found in inventory.")
        elif not book.is_available:
            print(f"[UNAVAILABLE] '{book.title}' is issued to {book.borrower}.")
        else:
            book.is_available = False
            book.borrower = member
            print(f"[SUCCESS] Issued '{book.title}' to {member}.")

    def return_book(self, book_id):
        book = self.catalog.get(book_id)
        if not book:
            print(f"[ERROR] Book ID '{book_id}' not found in inventory.")
        elif book.is_available:
            print(f"[WARNING] '{book.title}' is already marked as available.")
        else:
            prev = book.borrower
            book.is_available = True
            book.borrower = None
            print(f"[SUCCESS] '{book.title}' returned by {prev}.")


def demo_library_system():
    print("=== Lab Exercise 15: Library Management System (OOP & Inheritance) ===")
    lib = Library("SET Central Engineering Library")
    lib.add_book(Book("CS101", "Python Programming", "Guido van Rossum"))
    lib.add_book(Book("CS102", "Clean Architecture", "Robert C. Martin"))
    lib.add_book(Book("AI201", "Artificial Intelligence", "Stuart Russell"))
    lib.display_catalog()
    lib.issue_book("CS101", "Vishanth R")    # Valid issue
    lib.issue_book("CS101", "Aditi Roy")     # Conflict: already issued
    lib.issue_book("CS999", "Karan Verma")   # Non-existent book ID
    lib.return_book("CS101")                 # Valid return
    lib.return_book("CS101")                 # Duplicate return warning
    print()


# ==============================================================================
# Lab Exercise 16: Dice Simulator & Outcome Frequency Analysis (random module)
# ==============================================================================
class DiceSimulator:
    """Simulates multi-dice rolls, board game turns, and Monte Carlo trials."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self, num_dice=2):
        rolls = [random.randint(1, self.sides) for _ in range(num_dice)]
        return rolls, sum(rolls)

    def run_simulation(self, trials=10000, num_dice=2):
        freqs = {s: 0 for s in range(num_dice, num_dice * self.sides + 1)}
        for _ in range(trials):
            _, total = self.roll_dice(num_dice)
            freqs[total] += 1
        return freqs

    def display_analysis(self, trials=10000, num_dice=2):
        freqs = self.run_simulation(trials, num_dice)
        theo_probs = {
            2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
            8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
        }
        print(f"=== DICE SIMULATOR: {trials:,} ROLLS ({num_dice}D{self.sides}) ===")
        print(f"{'SUM':<5} {'FREQ':<7} {'OBS %':<9} {'THEO %':<9} {'DISTRIBUTION'}")
        print("-" * 55)
        for s in range(num_dice, num_dice * self.sides + 1):
            count, pct = freqs[s], (freqs[s] / trials) * 100
            theo, bars = theo_probs.get(s, 0.0), "█" * int(pct * 1.5)
            print(f"{s:<5} {count:<7} {pct:<9.2f} {theo:<9.2f} {bars}")
        print("-" * 55)
        print("Insight: Outcome 7 exhibits peak frequency (~16.7%), conforming to Gaussian curve.")
        print()


def demo_dice_simulator():
    print("=== Lab Exercise 16: Dice Simulator & Outcome Frequency Analysis ===")
    sim = DiceSimulator(sides=6)
    random.seed(131)
    print("--- BOARD GAME SAMPLE ROLLS ---")
    for t in range(1, 4):
        d, tot = sim.roll_dice(2)
        print(f"Turn {t}: Rolled {d} -> Total Move: {tot} spaces")
    print()
    sim.display_analysis(trials=10000, num_dice=2)


def main():
    print("=" * 60)
    print("LAB EXPERIMENTS – UNIT 5: OOP & Random Simulation")
    print("Developer: Vishanth R | Register: 25BTRAD131")
    print("=" * 60)
    print()
    demo_bank_account()
    demo_library_system()
    demo_dice_simulator()
    print("=" * 60)
    print("Unit 5 Lab Experiments executed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
