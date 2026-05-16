import re

def sanitize_input(user_input):
    # Remove leading and trailing spaces
    user_input = user_input.strip()

    # Allow only letters, numbers, spaces, @ . _
    sanitized = re.sub(r'[^a-zA-Z0-9@._ ]', '', user_input)

    return sanitized

# Get input from user
name = input("Enter your name: ")

# Sanitize input
clean_name = sanitize_input(name)

# Display result
print("\nSanitized Input:")
print(clean_name)
