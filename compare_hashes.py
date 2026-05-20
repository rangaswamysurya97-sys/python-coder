import hashlib

password1 = input("Enter first password: ")
password2 = input("Enter second password: ")

hash1 = hashlib.sha256(password1.encode()).hexdigest()
hash2 = hashlib.sha256(password2.encode()).hexdigest()

if hash1 == hash2:
    print("Hashes Match")
else:
    print("Hashes Do Not Match")
