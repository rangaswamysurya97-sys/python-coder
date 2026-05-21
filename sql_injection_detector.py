user_input = input("Enter input: ")

patterns = [
    "' OR '1'='1",
    "--",
    "DROP TABLE",
    "SELECT *"
]

for pattern in patterns:

    if pattern.lower() in user_input.lower():

        print("Possible SQL Injection Detected")
        break

else:

    print("Input Looks Safe")
