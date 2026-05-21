attempts = 0

while True:

    if attempts >= 3:

        print("Too Many Requests")
        break

    user = input("Enter request: ")

    print("Request Accepted")

    attempts += 1
