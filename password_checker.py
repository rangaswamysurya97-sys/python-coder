import re

password = input("Enter password: ")

length = len(password) >= 8
upper = re.search(r"[A-Z]", password)
lower = re.search(r"[a-z]", password)
digit = re.search(r"\d", password)
special = re.search(r"[@$!%*?&]", password)

if length and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")
