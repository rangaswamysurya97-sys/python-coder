print("1. Generate Hash")
print("2. Generate OTP")

choice = input("Choose option: ")

if choice == "1":

    import hashlib

    text = input("Enter text: ")

    hashed = hashlib.sha256(text.encode()).hexdigest()

    print("Hash:", hashed)

elif choice == "2":

    import random

    otp = random.randint(100000, 999999)

    print("OTP:", otp)

else:
    print("Invalid Option")
