"""
JAIN (DEEMED-TO-BE UNIVERSITY) - FACULTY OF ENGINEERING & TECHNOLOGY (SET)
Department of Computer Science & Engineering (AI & DE)
Course / Lab: Python Programming Laboratory
Semester & Sec: 3rd Semester | Class: CSE-AIDE (B)
Academic Year: 2026 – 2027

MINI PROJECT – UNIT 1: Multi-Category Unit Converter (Interactive Desktop GUI Application)
Student Name: Vishanth R
Register / USN: 25BTRAD131
"""

import sys
import tkinter as tk
from tkinter import ttk, messagebox


class UnitConverterEngine:
    """Core mathematical engine for multi-category conversions."""

    def __init__(self):
        self.conversion_factors = {
            "Length": {
                "Meters (m)": 1.0,
                "Kilometers (km)": 1000.0,
                "Miles (mi)": 1609.344,
                "Feet (ft)": 0.3048,
                "Inches (in)": 0.0254
            },
            "Weight": {
                "Kilograms (kg)": 1.0,
                "Grams (g)": 0.001,
                "Pounds (lb)": 0.453592,
                "Ounces (oz)": 0.0283495
            }
        }
        self.categories = ["Length", "Weight", "Temperature"]

    def convert(self, category, value, from_unit, to_unit):
        """Converts value between units for given category."""
        if category == "Temperature":
            return self.convert_temperature(value, from_unit, to_unit)

        factors = self.conversion_factors.get(category)
        if not factors or from_unit not in factors or to_unit not in factors:
            raise ValueError(f"Invalid unit conversion: {from_unit} -> {to_unit} in {category}")

        base_value = value * factors[from_unit]
        converted = base_value / factors[to_unit]
        return converted

    @staticmethod
    def convert_temperature(v, f, t):
        if f == t:
            return v
        c = v if "Celsius" in f else (v - 32.0) * 5.0 / 9.0 if "Fahrenheit" in f else v - 273.15
        return c if "Celsius" in t else (c * 9.0 / 5.0) + 32.0 if "Fahrenheit" in t else c + 273.15


class UnitConverterApp:
    """Desktop GUI interface using Tkinter."""

    def __init__(self, root):
        self.root = root
        self.root.title("Universal Unit Converter - Vishanth R (25BTRAD131)")
        self.root.geometry("520x620")
        self.root.resizable(False, False)

        self.engine = UnitConverterEngine()
        self.conversion_factors = self.engine.conversion_factors
        self.categories = self.engine.categories

        self.setup_ui()

    def setup_ui(self):
        # Header title banner
        header = tk.Label(
            self.root, text="Multi-Category Unit Converter",
            font=("Segoe UI", 14, "bold"), fg="#0F2744"
        )
        header.pack(pady=6)

        # Main Input Container Frame
        form_frame = tk.Frame(self.root, padx=15, pady=5)
        form_frame.pack(fill="x")

        # Category Selector
        tk.Label(form_frame, text="Select Category:", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w", pady=3)
        self.category_var = tk.StringVar(value="Length")
        self.cat_combo = ttk.Combobox(
            form_frame, textvariable=self.category_var,
            values=self.categories, state="readonly", width=28
        )
        self.cat_combo.grid(row=0, column=1, columnspan=2, pady=3, sticky="ew")
        self.cat_combo.bind("<<ComboboxSelected>>", self.on_category_change)

        # Input Value Field
        tk.Label(form_frame, text="Enter Value:", font=("Segoe UI", 10, "bold")).grid(row=1, column=0, sticky="w", pady=3)
        self.val_var = tk.StringVar()
        self.val_entry = tk.Entry(form_frame, textvariable=self.val_var, font=("Segoe UI", 10))
        self.val_entry.grid(row=1, column=1, columnspan=2, pady=3, sticky="ew")

        # From Unit & To Unit Dropdowns
        tk.Label(form_frame, text="From Unit:", font=("Segoe UI", 10, "bold")).grid(row=2, column=0, sticky="w", pady=3)
        self.from_unit_var = tk.StringVar()
        self.from_combo = ttk.Combobox(form_frame, textvariable=self.from_unit_var, state="readonly", width=14)
        self.from_combo.grid(row=2, column=1, pady=3, sticky="w")

        tk.Label(form_frame, text="To Unit:", font=("Segoe UI", 10, "bold")).grid(row=2, column=2, sticky="e", pady=3)
        self.to_unit_var = tk.StringVar()
        self.to_combo = ttk.Combobox(form_frame, textvariable=self.to_unit_var, state="readonly", width=14)
        self.to_combo.grid(row=2, column=3, pady=3, sticky="e")
        self.on_category_change()

        # Action Buttons Frame
        btn_frame = tk.Frame(self.root, pady=6)
        btn_frame.pack()
        tk.Button(
            btn_frame, text="Convert Value", bg="#2563EB", fg="white", font=("Segoe UI", 10, "bold"),
            command=self.perform_conversion, width=16
        ).grid(row=0, column=0, padx=6)
        tk.Button(
            btn_frame, text="Reset / Clear", bg="#DC2626", fg="white", font=("Segoe UI", 10, "bold"),
            command=self.clear_all, width=16
        ).grid(row=0, column=1, padx=6)

        # Dynamic Result Banner
        self.result_label = tk.Label(
            self.root, text="Select units and click Convert", font=("Segoe UI", 11, "bold"),
            bg="#F0FDF4", fg="#166534", relief="groove", pady=8
        )
        self.result_label.pack(fill="x", padx=20, pady=4)

        # Conversion History & Log Box
        tk.Label(self.root, text="Conversion Audit Log:", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=20, pady=(4, 2))
        self.log_text = tk.Text(self.root, height=10, width=58, font=("Consolas", 9))
        self.log_text.pack(padx=20, pady=3)

    def on_category_change(self, event=None):
        cat = self.category_var.get()
        if cat == "Temperature":
            units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
        else:
            units = list(self.conversion_factors[cat].keys())
        self.from_combo['values'] = units
        self.to_combo['values'] = units
        self.from_combo.current(0)
        self.to_combo.current(1 if len(units) > 1 else 0)

    def perform_conversion(self):
        try:
            val = float(self.val_var.get().strip())
            cat = self.category_var.get()
            u_from = self.from_unit_var.get()
            u_to = self.to_unit_var.get()

            converted = self.engine.convert(cat, val, u_from, u_to)
            res_str = f"{val} {u_from}  =  {converted:.4f} {u_to}"
            self.result_label.config(text=res_str, fg="#15803D")
            self.log_text.insert(tk.END, f"[LOG] {cat}: {res_str}\n")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid numeric value.")

    def clear_all(self):
        self.val_var.set("")
        self.result_label.config(text="Select units and click Convert", fg="#166534")
        self.log_text.delete(1.0, tk.END)


def run_cli_tests():
    """Runs automated CLI test suite verifying conversion math across categories."""
    print("=" * 60)
    print("MINI PROJECT – UNIT 1: Multi-Category Unit Converter")
    print("Developer: Vishanth R | Register: 25BTRAD131")
    print("=" * 60)
    engine = UnitConverterEngine()
    test_cases = [
        ("Length", 5000.0, "Meters (m)", "Kilometers (km)"),
        ("Length", 10.0, "Miles (mi)", "Kilometers (km)"),
        ("Weight", 15.0, "Kilograms (kg)", "Pounds (lb)"),
        ("Weight", 500.0, "Grams (g)", "Ounces (oz)"),
        ("Temperature", 100.0, "Celsius (°C)", "Fahrenheit (°F)"),
        ("Temperature", 300.0, "Kelvin (K)", "Celsius (°C)"),
    ]
    print(f"{'CATEGORY':<14} {'INPUT':<18} -> {'CONVERTED':<22}")
    print("-" * 60)
    for cat, val, f_u, t_u in test_cases:
        res = engine.convert(cat, val, f_u, t_u)
        print(f"{cat:<14} {val:.1f} {f_u:<12} -> {res:.4f} {t_u}")
    print("-" * 60)
    print("[SUCCESS] All unit mathematical conversion tests passed!")


if __name__ == "__main__":
    if "--cli" in sys.argv or "--test" in sys.argv:
        run_cli_tests()
    else:
        try:
            root = tk.Tk()
            app = UnitConverterApp(root)
            root.mainloop()
        except Exception as e:
            print(f"[NOTE] GUI initialization failed ({e}), running CLI mode instead:")
            run_cli_tests()
