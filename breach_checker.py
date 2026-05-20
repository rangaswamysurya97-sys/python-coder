breached_passwords = [
    "123456",
    "password",
    "admin"
]

password = input("Enter password: ")

if password in breached_passwords:

    print("Password Found In Breach List")

else:

    print("Password Not Found")
