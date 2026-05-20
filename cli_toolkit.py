print("1. Hash Generator")
print("2. OTP Generator")

choice = input("Choose option: ")

if choice == "1":

    import hashlib

    text = input("Enter text: ")

    print(
        hashlib.sha256(
            text.encode()
        ).hexdigest()
    )

elif choice == "2":

    import random

    print(
        random.randint(100000, 999999)
    )

else:

    print("Invalid Option")
