weak_passwords = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "welcome"
]

password = input("Enter password: ")

if password.lower() in weak_passwords:

    print("Weak Password Detected")

else:
    print("Password Looks Safer")
