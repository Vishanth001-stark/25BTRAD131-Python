"""
JAIN (DEEMED-TO-BE UNIVERSITY) - FACULTY OF ENGINEERING & TECHNOLOGY (SET)
Department of Computer Science & Engineering (AI & DE)
Course / Lab: Python Programming Laboratory
Semester & Sec: 3rd Semester | Class: CSE-AIDE (B)
Academic Year: 2026 – 2027

LAB EXPERIMENTS – UNIT 3: Data Structures (Lists & Dictionaries)
Student Name: Vishanth R
Register / USN: 25BTRAD131
"""


# ==============================================================================
# Lab Exercise 8: Contact Book Using Lists and Dictionaries (CRUD Operations)
# ==============================================================================
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, role):
        self.contacts[name] = {"Phone": phone, "Email": email, "Role": role}
        print(f"[SUCCESS] Added contact: {name} ({role})")

    def search_contact(self, name):
        c = self.contacts.get(name)
        if c:
            print(f"-> Found: {name} | Phone: {c['Phone']} | Role: {c['Role']} | Email: {c['Email']}")
        else:
            print(f"[!] Contact '{name}' not found.")
        return c

    def update_contact(self, name, phone=None, role=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]["Phone"] = phone
            if role:
                self.contacts[name]["Role"] = role
            print(f"[UPDATED] Modified contact details for: {name}")
        else:
            print(f"[!] Contact '{name}' not found.")

    def delete_contact(self, name):
        if self.contacts.pop(name, None):
            print(f"[DELETED] Removed contact: {name}")
        else:
            print(f"[!] Contact '{name}' not found.")

    def display_all(self):
        print("-" * 54)
        print(f"{'NAME':<12} {'PHONE':<13} {'ROLE':<12} {'EMAIL'}")
        print("-" * 54)
        for name, info in self.contacts.items():
            print(f"{name:<12} {info['Phone']:<13} {info['Role']:<12} {info['Email']}")
        print("-" * 54)


def demo_contact_book():
    print("=== Lab Exercise 8: Contact Book (CRUD Operations) ===")
    book = ContactBook()
    book.add_contact("Dr. Sharma", "9845012345", "sharma@jain.edu", "Faculty")
    book.add_contact("Vishanth R", "9123456789", "vishanth@aide.in", "Student")
    book.add_contact("Priya K", "9876543210", "priya@alumni.ac", "Alumni")
    book.search_contact("Vishanth R")
    book.update_contact("Vishanth R", phone="9988776655", role="Researcher")
    book.delete_contact("Priya K")
    book.display_all()
    print()


# ==============================================================================
# Lab Exercise 9: Student Grading System Using Dictionaries
# ==============================================================================
def evaluate_performance(marks_list):
    total = sum(marks_list)
    pct = total / len(marks_list)
    # Conditional logic for Grade boundaries and classification
    if pct >= 90:
        grade, status = "O (Outstanding)", "Distinction"
    elif pct >= 80:
        grade, status = "A+ (Excellent)", "First Class"
    elif pct >= 70:
        grade, status = "A (Very Good)", "First Class"
    elif pct >= 60:
        grade, status = "B (Good)", "Second Class"
    elif pct >= 50:
        grade, status = "C (Average)", "Pass Class"
    else:
        grade, status = "F (Fail)", "Needs Improvement"
    return total, pct, grade, status


def demo_student_grading():
    print("=== Lab Exercise 9: Student Grading System ===")
    students = {
        "25BTRAD131": {"Name": "Vishanth R", "Marks": [95, 92, 89]},
        "25BTRAD132": {"Name": "Aditi Roy", "Marks": [85, 78, 83]},
        "25BTRAD133": {"Name": "Karan Verma", "Marks": [74, 68, 71]},
        "25BTRAD134": {"Name": "Sneha Nair", "Marks": [58, 62, 55]},
        "25BTRAD135": {"Name": "Rahul Das", "Marks": [42, 38, 44]}
    }
    print("=" * 66)
    print(f"{'USN':<12} {'NAME':<12} {'TOTAL':<7} {'PCT(%)':<9} {'GRADE':<18} {'STATUS'}")
    print("=" * 66)
    for usn, info in students.items():
        tot, pct, grd, rmk = evaluate_performance(info["Marks"])
        print(f"{usn:<12} {info['Name']:<12} {tot:<7} {pct:<8.2f}% {grd:<18} {rmk}")
    print("=" * 66)
    print()


# ==============================================================================
# Lab Exercise 10: Frequency Counter Using Dictionaries
# ==============================================================================
def word_frequency_counter(sentence):
    clean_text = "".join(ch.lower() if ch.isalnum() or ch.isspace() else " " for ch in sentence)
    tokens = clean_text.split()
    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    return freq_dict


def element_frequency_counter(data_list):
    freq_dict = {}
    for item in data_list:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    return freq_dict


def demo_frequency_counter():
    print("=== Lab Exercise 10: Frequency Counter Using Dictionaries ===")
    # 1. Text Word Frequency Counter
    feedback = "Python is intuitive and powerful. Python libraries make Python great for AI and data science."
    word_counts = word_frequency_counter(feedback)
    print("--- Classroom Feedback Word Frequency Counter ---")
    print(f"{'WORD':<16} {'COUNT':<8} {'FREQUENCY DISTRIBUTION'}")
    print("-" * 52)
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{word:<16} {count:<8} {'#' * (count * 4)}")

    # 2. Element Frequency Counter
    preferences = ["AI & ML", "Cloud", "Data Engg", "AI & ML", "Cyber Sec", "AI & ML", "Data Engg"]
    pref_counts = element_frequency_counter(preferences)
    print("\n--- Domain Preference Survey Frequency Analysis ---")
    print(f"{'DOMAIN':<18} {'VOTES':<8} {'PERCENTAGE'}")
    print("-" * 52)
    total_votes = len(preferences)
    for domain, votes in sorted(pref_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (votes / total_votes) * 100
        print(f"{domain:<18} {votes:<8} {pct:.1f}%")
    print()


def main():
    print("=" * 60)
    print("LAB EXPERIMENTS – UNIT 3: Lists & Dictionaries")
    print("Developer: Vishanth R | Register: 25BTRAD131")
    print("=" * 60)
    print()
    demo_contact_book()
    demo_student_grading()
    demo_frequency_counter()
    print("=" * 60)
    print("Unit 3 Lab Experiments executed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
