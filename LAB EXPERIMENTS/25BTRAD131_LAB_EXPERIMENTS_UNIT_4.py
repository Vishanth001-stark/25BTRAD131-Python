"""
JAIN (DEEMED-TO-BE UNIVERSITY) - FACULTY OF ENGINEERING & TECHNOLOGY (SET)
Department of Computer Science & Engineering (AI & DE)
Course / Lab: Python Programming Laboratory
Semester & Sec: 3rd Semester | Class: CSE-AIDE (B)
Academic Year: 2026 – 2027

LAB EXPERIMENTS – UNIT 4: File Operations & CSV Data Processing
Student Name: Vishanth R
Register / USN: 25BTRAD131
"""

import csv
import os


# ==============================================================================
# Lab Exercise 11: Log File Reader Program
# ==============================================================================
def create_sample_log_file(filepath="server_app.log"):
    """Helper to generate a realistic sample log file for verification."""
    sample_logs = [
        "2026-11-15 10:00:01 [INFO] Server daemon initialized on port 8080.",
        "2026-11-15 10:01:23 [INFO] Connection established from 192.168.1.15.",
        "2026-11-15 10:02:45 [WARNING] High memory utilization: 82% threshold exceeded.",
        "2026-11-15 10:03:10 [INFO] Database query pool scaled to 16 workers.",
        "2026-11-15 10:04:55 [ERROR] Connection timeout to payment gateway gateway.paynet.internal.",
        "2026-11-15 10:05:02 [WARNING] Retry attempt 1/3 for gateway connection.",
        "2026-11-15 10:06:12 [ERROR] Fatal database dead-lock on transaction TXN-94819.",
        "2026-11-15 10:07:30 [INFO] Periodic health check passed for compute nodes.",
    ]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(sample_logs) + "\n")


def analyze_log_file(filepath="server_app.log"):
    """Analyzes a log file, counting occurrences of INFO, WARNING, and ERROR keywords."""
    print(f"=== Lab Exercise 11: Log File Analyzer ('{filepath}') ===")
    if not os.path.exists(filepath):
        print(f"[ERROR] Specified log file '{filepath}' not found.")
        return None
    if os.path.getsize(filepath) == 0:
        print(f"[WARNING] Log file '{filepath}' is empty (0 bytes).")
        return None

    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    recent_errors, total = [], 0

    with open(filepath, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            s = line.strip()
            if not s:
                continue
            total += 1
            for lvl in counts.keys():
                if f"[{lvl}]" in s:
                    counts[lvl] += 1
                    if lvl == "ERROR":
                        recent_errors.append((line_no, s))
                    break

    print("=" * 60)
    print(f"{'LOG LEVEL':<16} {'COUNT':<12} {'PERCENTAGE':<14} {'STATUS'}")
    print("=" * 60)
    for lvl, cnt in counts.items():
        pct = (cnt / total * 100) if total else 0
        status = "CRITICAL" if lvl == "ERROR" and cnt > 0 else "NORMAL"
        print(f"{lvl:<16} {cnt:<12} {pct:>6.1f}% {status}")
    print("=" * 60)
    print(f"Total Log Events: {total} | System Health: {'ALERT - Errors Found' if counts['ERROR'] else 'HEALTHY'}")
    if recent_errors:
        print("Critical Error Diagnostics:")
        for lno, msg in recent_errors:
            print(f" Line {lno:02d} -> {msg}")
    print()


# ==============================================================================
# Lab Exercise 12: Student Data Manager Using Files
# ==============================================================================
class StudentFileManager:
    def __init__(self, filepath="student_records.txt"):
        self.filepath = filepath

    def add_student(self, usn, name, branch, cgpa):
        if not (0.0 <= cgpa <= 10.0):
            print(f"[REJECTED] Invalid CGPA ({cgpa}). Must be 0.0 - 10.0.")
            return False
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(f"{usn}|{name}|{branch}|{cgpa:.2f}\n")
        print(f"[SUCCESS] Stored record: {name} (USN: {usn})")
        return True

    def search_student(self, usn_target):
        if not os.path.exists(self.filepath):
            print(f"[!] Records file not found.")
            return None
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    usn, name, branch, cgpa = parts
                    if usn.upper() == usn_target.upper():
                        print(f"-> Found: {name} | USN: {usn} | Branch: {branch} | CGPA: {cgpa}")
                        return parts
        print(f"[!] Record '{usn_target}' not found.")
        return None

    def update_student(self, usn_target, new_cgpa):
        if not os.path.exists(self.filepath):
            return False
        records, found = [], False
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    usn, name, branch, cgpa = parts
                    if usn.upper() == usn_target.upper():
                        records.append(f"{usn}|{name}|{branch}|{new_cgpa:.2f}\n")
                        found = True
                    else:
                        records.append(line)
                else:
                    records.append(line)
        if found:
            with open(self.filepath, "w", encoding="utf-8") as f:
                f.writelines(records)
            print(f"[UPDATED] Modified USN {usn_target} -> New CGPA: {new_cgpa:.2f}")
            return True
        print(f"[!] USN {usn_target} not found for update.")
        return False

    def display_all(self):
        if not os.path.exists(self.filepath):
            print("[!] Records file empty or missing.")
            return
        print("-" * 62)
        print(f"{'USN':<14} {'NAME':<16} {'BRANCH':<20} {'CGPA'}")
        print("-" * 62)
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    u, n, b, c = parts
                    print(f"{u:<14} {n:<16} {b:<20} {c}")
        print("-" * 62)


def demo_student_file_manager():
    print("=== Lab Exercise 12: Student Data Manager Using Persistent Files ===")
    manager = StudentFileManager("student_records.txt")
    # Clean previous demo run if exists
    if os.path.exists("student_records.txt"):
        os.remove("student_records.txt")
    manager.add_student("25BTRAD131", "Vishanth R", "CSE (AI & DE)", 9.45)
    manager.add_student("25BTRAD132", "Aditi Roy", "CSE (AI & DE)", 8.90)
    manager.add_student("25BTRAD133", "Karan Verma", "CSE (Cyber Sec)", 8.20)
    manager.search_student("25BTRAD131")
    manager.update_student("25BTRAD131", 9.68)
    manager.display_all()
    print()


# ==============================================================================
# Lab Exercise 13: CSV-Based Payroll Management System
# ==============================================================================
def create_sample_payroll_csv(csv_path="employee_payroll.csv"):
    """Creates a sample payroll CSV for automated verification."""
    data = [
        ["EmpID", "Name", "Designation", "BasicPay", "HRA", "DA"],
        ["EMP001", "Vishanth R", "Lead AI Engg", "85000", "25000", "15000"],
        ["EMP002", "Aditi Roy", "Data Architect", "75000", "22000", "12000"],
        ["EMP003", "Karan Verma", "DevOps Engineer", "55000", "16000", "9000"],
        ["EMP004", "Sneha Nair", "ML Engineer", "62000", "18000", "10000"],
    ]
    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def process_payroll_csv(csv_path="employee_payroll.csv"):
    """Reads employee records from a CSV file, calculates gross and deductions, and displays summary."""
    print(f"=== Lab Exercise 13: CSV Payroll System ('{csv_path}') ===")
    if not os.path.exists(csv_path):
        print(f"[ERROR] Payroll CSV '{csv_path}' not found.")
        return

    print("=" * 66)
    print(f"{'EMP ID':<8} {'NAME':<13} {'ROLE':<15} {'GROSS':<10} {'DEDUCT':<9} {'NET SALARY'}")
    print("=" * 66)
    tot_gross, tot_deduct, tot_net, count = 0.0, 0.0, 0.0, 0
    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            eid, name, role = row["EmpID"], row["Name"], row["Designation"]
            basic = float(row["BasicPay"])
            hra = float(row["HRA"])
            da = float(row["DA"])
            # Formulae: Gross = Basic + HRA + DA | Deductions = PF (12%) + Tax (5-10%)
            gross = basic + hra + da
            pf = 0.12 * basic
            tax = (0.10 * gross) if gross > 100000 else (0.05 * gross)
            deductions = pf + tax
            net = gross - deductions
            tot_gross += gross
            tot_deduct += deductions
            tot_net += net
            count += 1
            print(f"{eid:<8} {name:<13} {role:<15} {gross:<10.2f} {deductions:<9.2f} {net:<10.2f}")

    print("=" * 66)
    print(f"Employees Processed : {count} | Total Gross Payroll : Rs. {tot_gross:,.2f}")
    print(f"Statutory Deductions: Rs. {tot_deduct:,.2f} | Net Disbursement: Rs. {tot_net:,.2f}")
    print()


def main():
    print("=" * 60)
    print("LAB EXPERIMENTS – UNIT 4: File Operations & CSV Processing")
    print("Developer: Vishanth R | Register: 25BTRAD131")
    print("=" * 60)
    print()
    create_sample_log_file()
    analyze_log_file("server_app.log")
    demo_student_file_manager()
    create_sample_payroll_csv()
    process_payroll_csv("employee_payroll.csv")
    print("=" * 60)
    print("Unit 4 Lab Experiments executed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
