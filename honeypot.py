print("Fake Admin Login")

username = input("Username: ")
password = input("Password: ")

with open("honeypot_log.txt", "a") as file:
    file.write(f"Intruder -> {username}:{password}\n")

print("Access Denied")
