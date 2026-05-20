authorized_users = [
    "admin",
    "surya",
    "teacher"
]

username = input("Enter username: ")

if username in authorized_users:

    print("Access Granted")

else:

    print("Unauthorized Access Detected")
