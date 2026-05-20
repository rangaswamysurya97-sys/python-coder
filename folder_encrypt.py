from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

text = input("Enter text: ")

encrypted = cipher.encrypt(text.encode())

print("Encrypted:")
print(encrypted)

decrypted = cipher.decrypt(encrypted)

print("Decrypted:")
print(decrypted.decode())
