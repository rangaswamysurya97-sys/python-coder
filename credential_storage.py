import hashlib

username = input("Username: ")
password = input("Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

with open("credentials.txt", "a") as file:

    file.write(username + ":" + hashed_password + "\n")

print("Credentials Stored Securely")
