import re

# Common SQL Injection patterns
SQL_PATTERNS = [
    r"(\bor\b|\band\b).*=.*",     # OR 1=1
    r"(--)",                      # SQL comment
    r"(\bunion\b)",               # UNION keyword
    r"(\bselect\b)",              # SELECT keyword
    r"(\bdrop\b)",                # DROP keyword
    r"(\binsert\b)",              # INSERT keyword
    r"(\bdelete\b)",              # DELETE keyword
    r"(\bupdate\b)",              # UPDATE keyword
    r"('|\")",                    # Single or double quotes
    r"(;)",                       # Semicolon
]

def detect_sql_injection(user_input):
    detected = []

    for pattern in SQL_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            detected.append(pattern)

    if detected:
        print("\n[WARNING] Possible SQL Injection Detected!")
        print("\nDetected Patterns:")

        for item in detected:
            print("-", item)

    else:
        print("\n[SAFE] No SQL Injection Patterns Detected.")

# User input
text = input("Enter input to scan: ")

# Run detection
detect_sql_injection(text)
