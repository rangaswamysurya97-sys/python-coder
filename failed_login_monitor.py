attempts = {}

while True:
    username = input("Username: ")
    password = input("Password: ")

    if password != "admin123":
        attempts[username] = attempts.get(username, 0) + 1

        print("Login Failed")

        if attempts[username] >= 3:
            print("⚠ Account temporarily blocked")

    else:
        print("Login Successful")
        break
