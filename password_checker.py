import re

def check_password_strength(password):

    score = 0

    # Minimum length check
    if len(password) >= 8:
        score += 1

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1

    # Number check
    if re.search(r"[0-9]", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Password strength result
    print("\n===== Password Strength Report =====\n")

    if score == 5:
        print("Strength: VERY STRONG")
    elif score == 4:
        print("Strength: STRONG")
    elif score == 3:
        print("Strength: MEDIUM")
    elif score == 2:
        print("Strength: WEAK")
    else:
        print("Strength: VERY WEAK")

    print(f"Score: {score}/5")


# User input
password = input("Enter your password: ")

# Check password strength
check_password_strength(password)
