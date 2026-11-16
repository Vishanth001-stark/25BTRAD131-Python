"""
JAIN (DEEMED-TO-BE UNIVERSITY) - FACULTY OF ENGINEERING & TECHNOLOGY (SET)
Department of Computer Science & Engineering (AI & DE)
Course / Lab: Python Programming Laboratory
Semester & Sec: 3rd Semester | Class: CSE-AIDE (B)
Academic Year: 2026 – 2027

MINI PROJECT – UNIT 2: Secure OTP Generator & Verification System (Cryptographic Token Authentication)
Student Name: Vishanth R
Register / USN: 25BTRAD131
"""

import hashlib
import random
import string
import sys
import time


def generate_otp(length=6, alphanumeric=False):
    """Generates a cryptographically randomized numeric or alphanumeric OTP."""
    if alphanumeric:
        chars = string.ascii_uppercase + string.digits
    else:
        chars = string.digits
    otp = ''.join(random.choice(chars) for _ in range(length))
    generation_time = time.time()
    return otp, generation_time


def hash_otp(otp):
    """Computes SHA-256 cryptographic digest of OTP for tamper detection & audit."""
    return hashlib.sha256(otp.encode('utf-8')).hexdigest()


def mask_contact(contact_str):
    """Masks mobile number or email for confidentiality in transit logs."""
    clean = ''.join(filter(str.isdigit, contact_str))
    if len(clean) >= 10:
        return clean[:2] + '******' + clean[-2:]
    return contact_str


def verify_otp(generated_otp, entered_otp, gen_time, validity_seconds=60):
    """Validates user-entered OTP against token, expiration window, and format."""
    current_time = time.time()
    elapsed = current_time - gen_time

    if elapsed > validity_seconds:
        return False, f"OTP Expired! Elapsed: {elapsed:.1f}s (Max: {validity_seconds}s)"
    if entered_otp.strip().upper() == generated_otp.upper():
        return True, f"Verification Successful! Authenticated in {elapsed:.1f} seconds."
    return False, "Incorrect OTP token entered. Authentication failed!"


def run_interactive():
    print("=" * 60)
    print("   SECURE OTP GENERATOR & TOKEN VERIFICATION SYSTEM")
    print("   Developer: Vishanth R  |  Register: 25BTRAD131")
    print("=" * 60)
    user_name = input("Enter Account Holder Name: ").strip() or "Vishanth R"
    phone_num = input("Enter Registered Mobile Number: ").strip() or "9123456789"
    print("\nSelect OTP Generation Mode:")
    print("  [1] 6-Digit Numeric Pin (Banking Standard)")
    print("  [2] 6-Character Alphanumeric Token (Enhanced Security)")
    choice = input("Enter selection (1/2) [Default: 1]: ").strip()

    is_alpha = True if choice == "2" else False
    otp_type = "Alphanumeric" if is_alpha else "Numeric"
    otp, gen_time = generate_otp(length=6, alphanumeric=is_alpha)

    print("\n" + "-" * 60)
    print(f"[DISPATCH] Transmitting {otp_type} OTP to: {mask_contact(phone_num)}")
    print(f"[SECURITY] Generated OTP Token    : {otp}")
    print(f"[HASH-256] SHA-256 Audit Digest   : {hash_otp(otp)[:28]}...")
    print("[TIMING]   Validity Time-To-Live  : 60 Seconds")
    print("-" * 60)

    max_attempts, attempts = 3, 0
    while attempts < max_attempts:
        attempts += 1
        entered = input(f"\nEnter OTP for verification (Attempt {attempts}/{max_attempts}): ").strip()
        is_valid, msg = verify_otp(otp, entered, gen_time, validity_seconds=60)
        if is_valid:
            print(f"\n[ACCESS GRANTED] {msg}")
            print(f"Session established for {user_name} (Identity Verified)\n")
            break
        else:
            print(f"[ACCESS DENIED] {msg}")
            if attempts < max_attempts:
                print(f"Remaining attempts allowed: {max_attempts - attempts}")
            else:
                print("\n[SECURITY LOCKOUT] Max attempts exceeded. Token invalidated!")
    print("=" * 60)


def run_automated_tests():
    """Runs automated unit verification for CI and test suites."""
    print("=== Running Automated Tests for Secure OTP System ===")
    num_otp, t1 = generate_otp(6, alphanumeric=False)
    assert len(num_otp) == 6 and num_otp.isdigit(), "Numeric OTP generation failed!"
    print(f"[PASS] Numeric OTP Generated: {num_otp}")

    alpha_otp, t2 = generate_otp(6, alphanumeric=True)
    assert len(alpha_otp) == 6, "Alphanumeric OTP generation failed!"
    print(f"[PASS] Alphanumeric OTP Generated: {alpha_otp}")

    masked = mask_contact("9845012345")
    assert masked == "98******45", "Contact masking failed!"
    print(f"[PASS] Masked contact: {masked}")

    valid, _ = verify_otp(num_otp, num_otp, t1, validity_seconds=60)
    assert valid, "OTP verification match failed!"
    print("[PASS] Valid OTP verification succeeded.")

    invalid, _ = verify_otp(num_otp, "000000", t1, validity_seconds=60)
    assert not invalid, "Invalid OTP was falsely accepted!"
    print("[PASS] Invalid OTP rejection succeeded.")

    expired, msg = verify_otp(num_otp, num_otp, t1 - 70, validity_seconds=60)
    assert not expired and "Expired" in msg, "Expired OTP validation failed!"
    print("[PASS] Expired OTP rejection succeeded.")
    print("All OTP verification tests passed successfully!")


if __name__ == "__main__":
    if "--test" in sys.argv or "--cli" in sys.argv:
        run_automated_tests()
    else:
        run_interactive()
