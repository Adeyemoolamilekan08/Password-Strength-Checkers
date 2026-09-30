import re
import hashlib
import getpass


def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters for better security.")
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Check for common weak patterns
    common_passwords = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "password123",
        "admin",
        "admin123",
        "welcome",
        "letmein"
    ]

    if password.lower() in common_passwords:
        return "WEAK", ["This is a commonly used password. Choose a different one."]

    # Determine strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, feedback


def create_password_hash(password):
    """
    Demonstrates password hashing.

    SHA-256 is used here only to demonstrate the concept.
    Real applications should use a password-specific
    hashing algorithm such as Argon2, bcrypt, or scrypt.
    """

    password_hash = hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()

    return password_hash


def main():
    print("=" * 50)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    password = getpass.getpass("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print("\nPassword Analysis")
    print("-" * 30)

    print(f"Length: {len(password)} characters")

    print(
        "Lowercase letters:",
        "Yes" if re.search(r"[a-z]", password) else "No"
    )

    print(
        "Uppercase letters:",
        "Yes" if re.search(r"[A-Z]", password) else "No"
    )

    print(
        "Numbers:",
        "Yes" if re.search(r"\d", password) else "No"
    )

    print(
        "Special characters:",
        "Yes" if re.search(r"[^A-Za-z0-9]", password) else "No"
    )

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nYour password meets all the basic requirements.")

    # Hash demonstration
    print("\nHashing Demonstration")
    print("-" * 30)

    password_hash = create_password_hash(password)

    print("SHA-256 hash:")
    print(password_hash)

    print("\nNote: Never store or display real passwords in plain text.")


if __name__ == "__main__":
    main()