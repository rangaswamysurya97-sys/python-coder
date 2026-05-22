suspicious_words = [
    "urgent",
    "verify account",
    "bank",
    "password",
    "click here",
    "lottery",
    "winner"
]

email = input("Paste email content:\n").lower()

score = 0

for word in suspicious_words:
    if word in email:
        score += 1

print("\n--- Scan Result ---")

if score >= 3:
    print("⚠ High chance of phishing email")
elif score >= 1:
    print("⚠ Suspicious email")
else:
    print("✓ Email appears safe")
