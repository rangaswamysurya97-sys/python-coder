import random
import string

# Function to generate password
def generate_password(length):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# User input
length = int(input("Enter password length: "))

# Generate password
password = generate_password(length)

print("\nGenerated Password:")
print(password)
