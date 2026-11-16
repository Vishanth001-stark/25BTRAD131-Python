"""
JAIN (DEEMED-TO-BE UNIVERSITY) - FACULTY OF ENGINEERING & TECHNOLOGY (SET)
Department of Computer Science & Engineering (AI & DE)
Course / Lab: Python Programming Laboratory (25CSE204)
Semester & Sec: 3rd Semester | Class: CSE-AIDE (B)
Academic Year: 2026 – 2027

MINI PROJECT (UNIT 3) – PROBLEM SOLVING COMPONENT:
1. Classroom Attendance Tracker
2. Retail Sales Data Analytics System
Student Name: Vishanth R
Register / USN: 25BTRAD131
"""


# ==============================================================================
# Problem 1: Classroom Attendance Tracker
# ==============================================================================
class AttendanceTracker:
    """Classroom Attendance Tracking & Analytics System using Lists and Dictionaries.
    Stores student records, updates status, and computes attendance metrics.
    Developer: Vishanth R | Register: 25BTRAD131 | B.Tech CSE (AI & DE)
    """

    def __init__(self, course_code="25CSE204", course_name="Python Lab"):
        self.course_code = course_code
        self.course_name = course_name
        self.sessions = []  # List of lecture dates: ['03-Nov', '05-Nov', ...]
        self.students = {}  # Nested Dict: {usn: {'name': str, 'records': ['P', 'A', ...]}}

    def add_student(self, usn, name):
        """Enrolls student; pads existing sessions with '-' for late registrations."""
        if usn not in self.students:
            self.students[usn] = {"name": name, "records": ["-"] * len(self.sessions)}
            return True
        return False

    def record_session(self, session_date, attendance_map):
        """Appends class session date and logs 'P' or 'A' status for each student."""
        self.sessions.append(session_date)
        for usn, info in self.students.items():
            status = attendance_map.get(usn, "A").upper()
            info["records"].append(status)

    def update_attendance(self, usn, session_idx, new_status):
        """Updates/corrects an attendance record for a student on a specific session."""
        if usn in self.students and 0 <= session_idx < len(self.sessions):
            old = self.students[usn]["records"][session_idx]
            self.students[usn]["records"][session_idx] = new_status.upper()
            return old, new_status.upper()
        return None, None

    def get_student_metrics(self, usn):
        """Calculates total conducted sessions, attended count, and percentage."""
        records = self.students[usn]["records"]
        conducted = sum(1 for r in records if r in ["P", "A"])
        attended = sum(1 for r in records if r == "P")
        pct = (attended / conducted * 100.0) if conducted > 0 else 0.0
        return conducted, attended, pct

    def get_defaulters(self, threshold=75.0):
        """Identifies students below threshold and calculates classes needed to reach 75%."""
        defaulters = []
        for usn, info in self.students.items():
            cond, att, pct = self.get_student_metrics(usn)
            if pct < threshold:
                needed = max(0, int(-(-(0.75 * cond - att) // 0.25))) if cond > 0 else 0
                defaulters.append((usn, info["name"], att, cond, pct, needed))
        return defaulters

    def display_attendance_ledger(self, threshold=75.0):
        """Displays organized tabular ledger with session status and alerts."""
        header = f"{'USN':<12} {'STUDENT NAME':<16} " + " ".join(f"{d:>6}" for d in self.sessions)
        header += f" {'TOTAL':>5} {'PRES':>4} {'PCT(%)':>7} {'STATUS':<11}"
        print(header)
        print("-" * len(header))
        for usn, info in self.students.items():
            cond, att, pct = self.get_student_metrics(usn)
            st = "[ELIGIBLE]" if pct >= threshold else "[SHORTAGE]"
            row = f"{usn:<12} {info['name']:<16} " + " ".join(f"{x:>6}" for x in info["records"])
            row += f" {cond:>5} {att:>4} {pct:>6.1f}% {st:<11}"
            print(row)
        print("-" * len(header))


def demo_attendance_tracker():
    print("=" * 70)
    print("MINI PROJECT (UNIT 3) - PART 1: CLASSROOM ATTENDANCE TRACKER")
    print("=" * 70)
    tracker = AttendanceTracker()
    roster = [
        ("25BTRAD101", "Aarav Sharma"),
        ("25BTRAD102", "Bhavya Patel"),
        ("25BTRAD103", "Chaitra Rao"),
        ("25BTRAD104", "Divya Nair"),
        ("25BTRAD105", "Eshan Khan"),
        ("25BTRAD131", "Vishanth R"),
    ]
    for u, n in roster:
        tracker.add_student(u, n)

    sessions_data = [
        ("03-Nov", {"25BTRAD101": "P", "25BTRAD102": "P", "25BTRAD103": "P", "25BTRAD104": "A", "25BTRAD105": "P", "25BTRAD131": "P"}),
        ("05-Nov", {"25BTRAD101": "P", "25BTRAD102": "A", "25BTRAD103": "P", "25BTRAD104": "P", "25BTRAD105": "P", "25BTRAD131": "P"}),
        ("07-Nov", {"25BTRAD101": "P", "25BTRAD102": "A", "25BTRAD103": "A", "25BTRAD104": "P", "25BTRAD105": "A", "25BTRAD131": "P"}),
        ("10-Nov", {"25BTRAD101": "A", "25BTRAD102": "A", "25BTRAD103": "P", "25BTRAD104": "P", "25BTRAD105": "P", "25BTRAD131": "P"}),
        ("12-Nov", {"25BTRAD101": "P", "25BTRAD102": "P", "25BTRAD103": "P", "25BTRAD104": "A", "25BTRAD105": "P", "25BTRAD131": "P"}),
        ("14-Nov", {"25BTRAD101": "P", "25BTRAD102": "A", "25BTRAD103": "P", "25BTRAD104": "P", "25BTRAD105": "A", "25BTRAD131": "P"}),
    ]

    for dt, att in sessions_data:
        tracker.record_session(dt, att)

    # Regularize attendance via medical certificate
    tracker.update_attendance("25BTRAD103", 2, "P")  # Medical slip regularization

    tracker.display_attendance_ledger(threshold=75.0)

    defaulters = tracker.get_defaulters(threshold=75.0)
    print(f"\n[ALERT] Students with Attendance Shortage (<75%): {len(defaulters)}")
    for usn, name, att, cond, pct, needed in defaulters:
        print(f"  -> {usn} ({name}): Attended {att}/{cond} ({pct:.1f}%) | Consecutive Classes Needed: {needed}")
    print()


# ==============================================================================
# Problem 2: Retail Sales Data Analyzer
# ==============================================================================
class SalesDataAnalyzer:
    """Enterprise Sales Performance & Multi-Dataset Analyzer using Lists & Dictionaries.
    Tracks inventory, computes revenue, finds top-selling items, and compares datasets.
    Developer: Vishanth R | Register: 25BTRAD131 | B.Tech CSE (AI & DE)
    """

    def __init__(self, store_name="TechMatrix Retail Hub"):
        self.store_name = store_name
        self.products = {}  # Dict: {pid: {'name': str, 'category': str, 'unit_price': float, 'qty_sold': int}}

    def add_or_update_product(self, pid, name, category, unit_price, qty_sold=0):
        """Adds new product or updates details/pricing with additive quantity."""
        if pid in self.products:
            self.products[pid]["unit_price"] = unit_price
            self.products[pid]["qty_sold"] += qty_sold
        else:
            self.products[pid] = {
                "name": name, "category": category,
                "unit_price": unit_price, "qty_sold": qty_sold
            }

    def record_sales_batch(self, transactions):
        """Processes a batch list of sales [(pid, qty), ...] updating total units sold."""
        for pid, qty in transactions:
            if pid in self.products:
                self.products[pid]["qty_sold"] += qty

    def calculate_revenue_metrics(self):
        """Computes total gross sales, total units sold, and product-wise revenue."""
        summary = {}
        total_rev = 0.0
        total_units = 0
        for pid, data in self.products.items():
            rev = data["unit_price"] * data["qty_sold"]
            total_rev += rev
            total_units += data["qty_sold"]
            summary[pid] = {**data, "revenue": rev}

        for pid in summary:
            summary[pid]["share_pct"] = (summary[pid]["revenue"] / total_rev * 100) if total_rev > 0 else 0
        return total_rev, total_units, summary

    def get_top_performers(self):
        """Identifies top product by volume sold and top revenue generator."""
        top_qty = max(self.products.items(), key=lambda x: x[1]["qty_sold"])
        top_rev = max(self.products.items(), key=lambda x: x[1]["unit_price"] * x[1]["qty_sold"])
        return top_qty, top_rev

    @staticmethod
    def compare_datasets(ds_a, ds_b, label_a="Week 1", label_b="Week 2"):
        """Compares two sales datasets, evaluating unit growth, revenue variance & shifts."""
        rev_a = sum(p["unit_price"] * p["qty_sold"] for p in ds_a.values())
        rev_b = sum(p["unit_price"] * p["qty_sold"] for p in ds_b.values())
        units_a = sum(p["qty_sold"] for p in ds_a.values())
        units_b = sum(p["qty_sold"] for p in ds_b.values())
        growth_rev = ((rev_b - rev_a) / rev_a * 100) if rev_a > 0 else 0.0
        growth_units = ((units_b - units_a) / units_a * 100) if units_a > 0 else 0.0
        return (rev_a, rev_b, growth_rev), (units_a, units_b, growth_units)


def demo_sales_analyzer():
    print("=" * 70)
    print("MINI PROJECT (UNIT 3) - PART 2: RETAIL SALES DATA ANALYZER")
    print("=" * 70)
    analyzer = SalesDataAnalyzer()
    initial_inventory = [
        ("P101", "Wireless Mouse", "Electronics", 650.0, 45),
        ("P102", "Mechanical Keyboard", "Electronics", 2650.0, 24),
        ("P103", "USB-C Hub Multiport", "Accessories", 1450.0, 35),
        ("P104", "Noise-Cancel Headset", "Audio", 4200.0, 18),
        ("P105", "Portable SSD 1TB", "Storage", 7500.0, 12),
        ("P106", "Laptop Cooling Stand", "Accessories", 950.0, 56),
    ]
    for pid, nm, cat, pr, q in initial_inventory:
        analyzer.add_or_update_product(pid, nm, cat, pr, q)

    analyzer.add_or_update_product("P101", "Wireless Mouse", "Electronics", 650.0, 10)  # Restock sale update
    total_rev, total_units, summary = analyzer.calculate_revenue_metrics()
    top_qty, top_rev = analyzer.get_top_performers()

    print(f"STORE REVENUE SUMMARY: {analyzer.store_name.upper()}")
    print("-" * 70)
    print(f"{'PID':<6} {'NAME':<24} {'CATEGORY':<14} {'PRICE':<8} {'QTY':<5} {'REVENUE':<10} {'SHARE'}")
    print("-" * 70)
    for pid, d in summary.items():
        print(f"{pid:<6} {d['name']:<24} {d['category']:<14} {d['unit_price']:<8.0f} {d['qty_sold']:<5} {d['revenue']:<10.0f} {d['share_pct']:.1f}%")
    print("-" * 70)
    print(f"Gross Revenue: Rs.{total_rev:,.2f} | Total Units Sold: {total_units}")
    print(f"Top by Volume:  {top_qty[1]['name']} ({top_qty[1]['qty_sold']} units sold)")
    top_rev_val = top_rev[1]['unit_price'] * top_rev[1]['qty_sold']
    print(f"Top by Revenue: {top_rev[1]['name']} (Rs.{top_rev_val:,.2f})")
    print()


def main():
    demo_attendance_tracker()
    demo_sales_analyzer()
    print("=" * 70)
    print("Unit 3 Mini Project executed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
